import json
import random
from django.http import StreamingHttpResponse, JsonResponse, HttpResponse #для потоковой передачи данных
from django.views import View
from .models import Person, Result
import time

class RaceSimulationView(View):
    def get(self, request):
        try:
            partics = list(Person.objects.all()) #получение всех участников из бд
            def generate_race_data(): #генератор потоковых данных

                #Инициализация данных участников
                partic_data = []
                for partic in partics:
                    partic_data.append({
                        'id': partic.id,
                        'distance': 0.0, # Пройденная дистанция
                        'speed': 0.0, # Текущая скорость
                        'time_passed': 0.0, # Прошедшее время
                        'phase': 'waiting', # Текущая фаза
                        'finished': False,
                        # Параметры с рандомизацией:
                        'reaction': float(partic.time_of_reaction) * random.uniform(0.9, 1.1),
                        'accel': float(partic.acceleration) * random.uniform(0.9, 1.1),
                        'max_speed': float(partic.max_speed) * random.uniform(0.9, 1.1),
                        'decel': float(partic.coef) * random.uniform(0.9, 1.1),
                        'stamina': random.uniform(0.9, 1.0)
                    })
                
                start_time = time.time()
                interval = 0.1  # 100 ms
                winner = None
                
                while True: #основной цикл симуляции
                    elapsed = time.time() - start_time
                    c_time = round(elapsed, 1)
                    c_state = {
                        'time': c_time,
                        'racers': {},
                        'winner': winner
                    }
                    
                    finish = []
                    
                    for data in partic_data: 
                        if data['finished']:
                            c_state['racers'][data['id']] = {
                                'distance': 0.0,
                                'speed': 0.0,
                                'finished': True
                            }
                            continue
                            
                        data['time_passed'] += interval
                        
                        # Фазы движения

                        #фаза ожидания: на 100-ой мс переходит в стадию "ускорение"
                        if data['phase'] == 'waiting': 
                            if data['time_passed'] >= data['reaction']:
                                data['phase'] = 'accelerating'
                        #фаза ускорения: скорость = мин(скорость + уск*0.1 или скорость)
                        elif data['phase'] == 'accelerating':
                            data['speed'] = min(data['speed'] + data['accel'] * interval,data['max_speed'])
                            #если скорость = макс
                            if data['speed'] >= data['max_speed']:
                                data['phase'] = 'const'
                        #фаза постоянной скорости(после 80 метров след. стадия)
                        elif data['phase'] == 'const' and data['distance'] > 80:
                            data['phase'] = 'decelerating'
                        
                        elif data['phase'] == 'decelerating':
                            stamina_effect = 1 - (data['time_passed']/30) * (1 - data['stamina'])
                            data['speed'] = max(
                                data['speed'] + data['decel'] * interval * stamina_effect,
                                data['max_speed'] * 0.3
                            )
                        
                        # Обновление дистанции
                        data['distance'] += data['speed'] * interval * random.uniform(0.98, 1.02)
                        
                        if data['distance'] >= 100:
                            data['distance'] = 100
                            data['finished'] = True
                            data['finished_time'] = c_time
                            finish.append(data['id'])
                        
                        c_state['racers'][data['id']] = {
                            'distance': round(100 - data['distance'], 2),
                            'speed': round(data['speed'], 2),
                            'finished': data['finished']
                        }
                    
                    if finish and not winner:
                        winner = random.choice(finish) if len(finish) > 1 else finish[0]
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


def result_stat(request):       #1 - id, 2 - место
    obj = Person.objects.values_list('pk', 'acceleration', 'max_speed')

    vocabulary = {elem[0]: elem[1] + elem[2] + random.randint(-2, 2) for elem in obj}
    vocabulary = sorted(vocabulary.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    for row, place in zip(vocabulary, range(1, len(vocabulary) + 1)):
        Result.objects.update_or_create(
            person=row[0],
            defaults={'value': place}
        )
        
    results = Result.objects.select_related('person').order_by('value')
    output = "<br>".join([f"{r.person.pk}: {r.value} место" for r in results])
    return HttpResponse(output)
    
    
    
    

