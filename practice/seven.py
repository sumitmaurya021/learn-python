import requests

latitude, longitude = 23.114358, 72.5384318

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["current_weather"]["temperature"]
    print(f"current temperature is {temp}C")
else:
    print(f"error {response.status_code}")
