import requests

cidade = input('Nome da Cidade: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&id=524901&units=metric&APPID=f009815646ea75014127d2fd7d0b4860'

r = requests.get(url)

clima = r.json()

print(f"A temperatura em {cidade} é de {clima['main']['temp']} ºC.")


