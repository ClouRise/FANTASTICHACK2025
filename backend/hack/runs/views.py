import json
import random
import time
from collections import defaultdict
from django.http import JsonResponse, StreamingHttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.db.models import Count
from .models import Person, Result

class PersonAPI(View):
    def get(self, request, person_id=None):
        try:
            if person_id is None:
                persons = list(Person.objects.all().values(
                    'id',
                    'time_of_reaction',
                    'acceleration',
                    'max_speed',
                    'coef',
                    'color'
                ))
                return JsonResponse({'persons': persons}, safe=False)
            else:
                person = Person.objects.get(pk=person_id)
                return JsonResponse({
                    'id': person.id,
                    'time_of_reaction': str(person.time_of_reaction),
                    'acceleration': str(person.acceleration),
                    'max_speed': str(person.max_speed),
                    'coef': str(person.coef),
                    'color': person.color
                })
        
        except Person.DoesNotExist:
            return JsonResponse(
                {'error': f'Участник с ID {person_id} не найден'},
                status=404
            )
        except Exception as e:
            return JsonResponse(
                {'error': 'Ошибка сервера', 'details': str(e)},
                status=500
            )

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def put(self, request, person_id):
        try:
            person = Person.objects.get(pk=person_id)
            data = json.loads(request.body)
            
            allowed_fields = ['time_of_reaction', 'acceleration', 'max_speed', 'coef', 'color']
            for field in allowed_fields:
                if field in data:
                    setattr(person, field, data[field])
            
            person.full_clean()
            person.save()
            
            return JsonResponse({
                'status': 'success',
                'message': f'Данные участника {person_id} обновлены'
            })
        
        except Person.DoesNotExist:
            return JsonResponse(
                {'error': f'Участник с ID {person_id} не найден'},
                status=404
            )
        except ValidationError as e:
            return JsonResponse(
                {'error': 'Ошибка валидации', 'details': str(e)},
                status=400
            )
        except Exception as e:
            return JsonResponse(
                {'error': 'Ошибка сервера', 'details': str(e)},
                status=500
            )

class RaceSimulationView(View):
    def _calculate_probabilities(self):
        results = Result.objects.values('person', 'value').annotate(count=Count('value'))
        
        prob_dict = defaultdict(lambda: {1:0, 2:0, 3:0, 4:0, 5:0, 6:0})
        for item in results:
            prob_dict[item['person']][item['value']] = item['count']
        
        probabilities = {}
        for person_id in prob_dict:
            total = sum(prob_dict[person_id].values())
            probabilities[person_id] = {
                place: round((count + 1) / (total + 6), 3)
                for place, count in prob_dict[person_id].items()
            }
        
        return probabilities

    def _save_final_results(self, finished_participants):
        sorted_results = sorted(
            finished_participants,
            key=lambda x: (x['finished_time'], random.gauss(0, 0.1)) 
        )
        
        final_places = {
            p['id']: i+1 for i, p in enumerate(sorted_results)
        }
        for person_id, place in final_places.items():
            Result.objects.create(
                person_id=person_id,
                value=place
            )
        
        return final_places

    def get(self, request):
        try:
            participants = list(Person.objects.all())
            
            def generate_race_data():
                race_data = []
                finished_participants = []
                
                for p in participants:
                    reaction_time = float(p.time_of_reaction) * random.uniform(0.7, 1.3)
                    accel = float(p.acceleration) * random.uniform(0.7, 1.3)
                    max_speed = float(p.max_speed) * random.uniform(0.7, 1.3)
                    decel = float(p.coef) * random.uniform(0.7, 1.3)
                    
                    race_data.append({
                        'id': p.id,
                        'color': p.color,
                        'distance': 0.0,
                        'speed': 0.0,
                        'time_passed': 0.0,
                        'phase': 'waiting',
                        'finished': False,
                        'reaction': reaction_time,
                        'accel': accel,
                        'max_speed': max_speed,
                        'decel': decel,
                        'stamina': random.uniform(0.7, 1.0),
                        'finished_time': None,
                        'random_factor': random.uniform(0.9, 1.1)
                    })
                
                probabilities = self._calculate_probabilities()
                start_time = time.time()
                interval = 0.1
                
                while True:
                    elapsed = time.time() - start_time
                    current_time = round(elapsed, 1)
                    state = {
                        'time': current_time,
                        'racers': {},
                        'winner': None,
                        'final_results': None
                    }
                    
                    for data in race_data:
                        if data['finished']:
                            state['racers'][data['id']] = {
                                'distance': 0,
                                'speed': 0,
                                'finished': True,
                                'color': data['color'],
                                'probabilities': None
                            }
                            continue
                            
                        data['time_passed'] += interval
                        
                        if data['phase'] == 'waiting':
                            if data['time_passed'] >= data['reaction']:
                                data['phase'] = 'accelerating'
                        elif data['phase'] == 'accelerating':
                            data['speed'] = min(
                                data['speed'] + data['accel'] * interval * data['random_factor'],
                                data['max_speed']
                            )
                            if data['speed'] >= data['max_speed']:
                                data['phase'] = 'const'
                        elif data['phase'] == 'const' and data['distance'] > 80:
                            data['phase'] = 'decelerating'
                        elif data['phase'] == 'decelerating':
                            stamina_effect = 1 - (data['time_passed']/30) * (1 - data['stamina'])
                            data['speed'] = max(
                                data['speed'] + data['decel'] * interval * stamina_effect * data['random_factor'],
                                data['max_speed'] * 0.3
                            )
                        
                        data['distance'] += data['speed'] * interval * random.uniform(0.95, 1.05)
                        
                        if data['distance'] >= 100 and not data['finished']:
                            data['distance'] = 100
                            data['finished'] = True
                            data['finished_time'] = current_time
                            finished_participants.append(data.copy())
                            
                        state['racers'][data['id']] = {
                            'distance': round(100 - data['distance'], 2),
                            'speed': round(data['speed'], 2),
                            'finished': data['finished'],
                            'color': data['color'],
                            'probabilities': probabilities if len(finished_participants) == len(participants) else None
                        }
                    
                    if len(finished_participants) == len(participants):
                        final_results = self._save_final_results(finished_participants)
                        state['final_results'] = final_results
                        state['probabilities'] = probabilities
                        state['winner'] = next(iter(final_results)) 
                    
                    yield f"data: {json.dumps(state)}\n\n"
                    
                    if all(data['finished'] for data in race_data):
                        break
                        
                    time.sleep(max(0, interval - (time.time() - start_time) % interval))
            
            response = StreamingHttpResponse(
                generate_race_data(),
                content_type='text/event-stream'
            )
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            return response
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def result_stat(request):
    try:
        with open('n.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            n = data[0]['n']
            
            
            participants = list(Person.objects.values_list('pk', 'acceleration', 'max_speed'))
            
            for _ in range(n):    

                results = {
                    p[0]: p[1] + p[2] + random.gauss(0, 1.5) 
                    for p in participants
                }
                sorted_results = sorted(results.items(), key=lambda x: (x[1], random.random()), reverse=True)
                
                for (person_id, _), place in zip(sorted_results, range(1, len(participants) + 1)):
                    Result.objects.create(
                        person_id=person_id,
                        value=place
                    )

            return JsonResponse({
                'status': 'success',
                'iterations': n,
                'created': len(participants)
            })
    except Exception as e:
        return JsonResponse({'error': str(e)}, sttus=500)

def get_persons(request):
    persons = list(Person.objects.all().values('id', 'color'))
    return JsonResponse({'persons': persons}, safe=False)