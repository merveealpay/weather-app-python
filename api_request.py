import requests
import json

api_url = "http://api.openweathermap.org/data/2.5/weather?q=Istanbul,tr&APPID=c2f937dd854fd8a1ac670111496b7f0e"

response = requests.get(api_url)

json_response = json.loads(response.text)

print("temp : " + str(json_response["main"]["temp"] - 273 ) + " *C")