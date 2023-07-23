import requests
import subprocess

url = 'https://ilock.apple.com/'

# Коды, которые нужно отправить
codes = ['SHAi', 'RuCode', 'Jain']

# Создание словаря с данными для POST-запроса
data = {'codes': codes}

# Отправка POST-запроса
response = requests.post(url, data=data)

# Проверка статуса ответа
if response.status_code == 200:
    print('POST-запрос успешно отправлен.')
else:
    print('Ошибка при отправке POST-запроса.')

# Команда для выполнения
command = ['ideviceinfo']

# Выполнение команды с помощью subprocess
result = subprocess.run(command, capture_output=True, text=True)

# Вывод результатов
print(result.stdout)
