import requests

# вывод текста ответа
response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)