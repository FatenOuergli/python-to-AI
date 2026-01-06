
import requests 

def get_weather(latitude,longitude):
    response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m")
    data=response.json()
    return data['hourly']

paris=get_weather(48.85,2.35)
japan=get_weather(35.68,139.77)
america=get_weather(40.71,-74.01)

print(f"Paris: {paris}°C")
print(f"Japan: {japan}°C")
print(f"America: {america}°C")