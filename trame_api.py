import requests

ville = input("Where ? ")

def log_ville(city):

    adress = 'http://api.openweathermap.org/data/2.5/weather?appid=7eb7eebdc32e8e2def3bb47154c712d3&q='
    try:
        url = adress + city
        json_data = requests.get(url).json()
        info = json_data['weather'][0]['description']
    except KeyError:
        print("Je ne trouve pas de villes de ce nom la ")
        quit()

    temp = json_data['main']['temp']
    temp = temp - 273
    print('Température de ' + str(int(temp)) + '°c a ' + str(city))

    if info == 'overcast clouds':
        info = 'ciel nuageux'

    if info == 'light rain':
        info = 'pluie légére'

    if info == 'scattered clouds':
        info = 'nuage épars'

    if info == 'broken clouds':
        info = 'nuage bas'

    return info

print(log_ville(ville))