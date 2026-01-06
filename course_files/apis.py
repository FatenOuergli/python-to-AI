import requests

latitude=48.85
longitude=2.35

url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
response=requests.get(url)
data=response.json() 
data.keys
data["current_weather_units"]
print(data)


