import datetime

def log_view(rezhim):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'Режим передачи данных: {rezhim}-порт. Время запроса: {str(datetime.datetime.now())}\n')
