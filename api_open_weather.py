import requests
from pprint import pprint

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat="
                 "44,83663&lon=-0,58105&exclude=current&appid=7eb7eebdc32e8e2def3bb47154c712d3")

data = response.json()
pprint(data['daily'])

