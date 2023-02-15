import requests

# вывод текста ответа
response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)

# тест из домашнего задания.
getText = requests.get("https://playground.learnqa.ru/api/get_text")
print(getText.text)