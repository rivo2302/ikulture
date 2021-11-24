import requests
import json

def meteo (region):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={region}&appid=b8cf04a5f89db5f7bfb1e16966ac7848&units=metric&lang=fr')
    data = json.loads(response.text)
    result = {}
    result["temp"] = data["main"]["temp"]
    result["desc"] = data["weather"][0]["description"]
    return result 
