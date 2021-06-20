import requests
import json

api_url = "http://api.openweathermap.org/data/2.5/weather?q=Istanbul,tr&" + API_KEY

response = requests.get(api_url)

json_response = json.loads(response.text)

print("temp : " + str(json_response["main"]["temp"] - 273 ) + " *C")
