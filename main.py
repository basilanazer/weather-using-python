import requests
import json
response=requests.get("https://goweather.herokuapp.com/weather/trivandrum")
data=json.loads(response.text)
temp=data.get('temperature')
des=data.get('description')
print('temperature : ',temp)
print(des)
