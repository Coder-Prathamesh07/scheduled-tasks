import requests
from twilio.rest import Client
import os
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
PARAMETERS = {
    "lat":45.815010,
    "lon":15.981919,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(url=weather_endpoint,params=PARAMETERS)
data = response.json()
will_rain = False
for hour_data in data["list"]:
    condition_code=(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today remember to bring an Umbrella",
        from_="+16623462114",
        to="+917204597349",
    )
