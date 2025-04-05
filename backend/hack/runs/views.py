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
                        'color': partic.color, 
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
                                'finished': True,
                                'color': data['color']
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
                            'finished': data['finished'],
                            'color': data['color']
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


def result_stat(request):
    with open('n.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        n = data[0]['n']  # Получаем количество итераций из JSON

        for _ in range(n):    
            # Получаем всех участников с их характеристиками
            participants = Person.objects.values_list('pk', 'acceleration', 'max_speed')
            
            # Рассчитываем результаты с небольшой случайной вариацией
            results = {
                person_id: float(accel) + float(max_speed) + random.randint(-2, 2)
                for person_id, accel, max_speed in participants
            }
            
            # Сортируем участников по результатам (лучший первый)
            sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    
            # Создаем новые записи Result для каждого участника
            for position, (person_id, _) in enumerate(sorted_results, start=1):
                Result.objects.create(
                    person_id=person_id,
                    value=position
                )
        
        return JsonResponse({
            'status': 'success', 
            'created': n * len(results),
            'message': f'Создано {n * len(results)} новых записей Result'
        })
    
def get_persons(request):
    persons = list(Person.objects.all().values(
        'id',
        'color'  # Добавляем color в вывод
    ))
    return JsonResponse({'persons': persons}, safe=False)


