from chatterbot import ChatBot
from wit import Wit

import forecastio
import datetime

chatbot = ChatBot(
    'Kenzo the Weather Guy',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=['chatterbot_weather.weather_adapter.WeatherLogicAdapter'])
    
user_lat = input("Hey there! I'm Kenzo the Weather Guy. Could you please enter your latitude?: ")
user_lng = input("Thank you and can I have your longitude now?: ")

api_key = '64c380d2d609333c01f0f093085ae740'
lat = user_lat
lng = user_lng

request = input("Do you want the hourly or current forecast?: ")
if request == 'hourly':
    forecast = forecastio.load_forecast(api_key, lat, lng),
    byHour = forecast.hourly(),
    print byHour.summary,
    print byHour.icon,
    
elif request == 'current':
    forecast = forecastio.load_forecast(api_key, lat, lng)
    byCurrent = forecast.currently()
    print byCurrent.summary
    print byCurrent.icon
else:
    print("Whoa lol I have no idea what you said just then")



