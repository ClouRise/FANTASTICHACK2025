import json
import random
from django.http import StreamingHttpResponse, JsonResponse, HttpResponse
from django.views import View
from .models import Person, Result
import time
from collections import defaultdict
from django.db.models import Count
from django.core.cache import cache
from django.utils import timezone
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
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

    @csrf_exempt
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
    def _get_cached_probabilities(self):
        cache_key = 'race_probabilities_cache'
        probabilities = cache.get(cache_key)
        if not probabilities:
            probabilities = self._calculate_probabilities()
            cache.set(cache_key, probabilities, 300)
        return probabilities

    def _calculate_probabilities(self):
        results = Result.objects.values('person', 'value').annotate(count=Count('value'))
        
        prob_dict = defaultdict(lambda: {1:0, 2:0, 3:0, 4:0, 5:0, 6:0})
        for item in results:
            prob_dict[item['person']][item['value']] = item['count']
        
        probabilities = {}
        for person_id in prob_dict:
            total = max(1, sum(prob_dict[person_id].values()))
            probabilities[person_id] = {
                place: round(count/total, 3)
                for place, count in prob_dict[person_id].items()
            }
        
        return probabilities

    def _save_final_results(self, finished_participants):
        sorted_results = sorted(
            finished_participants,
            key=lambda x: x['finished_time']
        )
        
        final_places = {
            p['id']: i+1 for i, p in enumerate(sorted_results)
        }
        
        # Создаем новые записи без удаления старых
        for person_id, place in final_places.items():
            Result.objects.create(
                person_id=person_id,
                value=place
            )
        
        return final_places

    def get(self, request):
        try:
            partics = list(Person.objects.all())
            
            def generate_race_data():
                partic_data = []
                finished_participants = []
                
                for partic in partics:
                    partic_data.append({
                        'id': partic.id,
                        'color': partic.color,
                        'distance': 0.0,
                        'speed': 0.0,
                        'time_passed': 0.0,
                        'phase': 'waiting',
                        'finished': False,
                        'reaction': float(partic.time_of_reaction) * random.uniform(0.9, 1.1),
                        'accel': float(partic.acceleration) * random.uniform(0.9, 1.1),
                        'max_speed': float(partic.max_speed) * random.uniform(0.9, 1.1),
                        'decel': float(partic.coef) * random.uniform(0.9, 1.1),
                        'stamina': random.uniform(0.9, 1.0),
                        'finished_time': None
                    })
                
                probabilities = self._get_cached_probabilities()
                start_time = time.time()
                interval = 0.1
                winner = None
                final_results = None
                
                while True:
                    elapsed = time.time() - start_time
                    c_time = round(elapsed, 1)
                    c_state = {
                        'time': c_time,
                        'racers': {},
                        'winner': winner,
                        'probabilities': probabilities,
                        'final_results': final_results
                    }
                    
                    for data in partic_data: 
                        if data['finished']:
                            c_state['racers'][data['id']] = {
                                'distance': 0.0,
                                'speed': 0.0,
                                'finished': True,
                                'color': data['color']
                            }
                            continue
                            
                        data['time_passed'] += interval
                        
                        if data['phase'] == 'waiting': 
                            if data['time_passed'] >= data['reaction']:
                                data['phase'] = 'accelerating'
                        elif data['phase'] == 'accelerating':
                            data['speed'] = min(data['speed'] + data['accel'] * interval, data['max_speed'])
                            if data['speed'] >= data['max_speed']:
                                data['phase'] = 'const'
                        elif data['phase'] == 'const' and data['distance'] > 80:
                            data['phase'] = 'decelerating'
                        elif data['phase'] == 'decelerating':
                            stamina_effect = 1 - (data['time_passed']/30) * (1 - data['stamina'])
                            data['speed'] = max(
                                data['speed'] + data['decel'] * interval * stamina_effect,
                                data['max_speed'] * 0.3
                            )
                        
                        data['distance'] += data['speed'] * interval * random.uniform(0.98, 1.02)
                        
                        if data['distance'] >= 100 and not data['finished']:
                            data['distance'] = 100
                            data['finished'] = True
                            data['finished_time'] = c_time
                            finished_participants.append(data.copy())
                        
                        c_state['racers'][data['id']] = {
                            'distance': round(100 - data['distance'], 2),
                            'speed': round(data['speed'], 2),
                            'finished': data['finished'],
                            'color': data['color']
                        }
                    
                    if len(finished_participants) == len(partics) and final_results is None:
                        final_results = self._save_final_results(finished_participants)
                        c_state['final_results'] = final_results
                    
                    if finished_participants and not winner:
                        winner = random.choice([p['id'] for p in finished_participants]) if len(finished_participants) > 1 else finished_participants[0]['id']
                        c_state['winner'] = winner
                    
                    yield f"data: {json.dumps(c_state)}\n\n"
                    
                    if all(data['finished'] for data in partic_data):
                        break
                        
                    time.sleep(max(0, interval - (time.time() - start_time) % interval))
            
            response = StreamingHttpResponse(
                generate_race_data(),
                content_type='text/event-stream'
            )
            response['Cache-Control'] = 'no-cache'
            return response
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def result_stat(request):
    with open('n.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        n = data[0]['n']

        for _ in range(n):    
            obj = Person.objects.values_list('pk', 'acceleration', 'max_speed')
            vocabulary = {
                elem[0]: elem[1] + elem[2] + random.randint(-2, 2) 
                for elem in obj
            }
            vocabulary = sorted(vocabulary.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
            for row, place in zip(vocabulary, range(1, len(vocabulary) + 1)):
                Result.objects.create(
                    person_id=row[0],
                    value=place
                )
        
        return JsonResponse({
            'status': 'success',
            'iterations': n,
            'created': len(vocabulary)
        })

def get_persons(request):
    persons = list(Person.objects.all().values('id', 'color'))
    return JsonResponse({'persons': persons}, safe=False)
