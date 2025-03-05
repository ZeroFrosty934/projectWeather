import datetime as dt 
import requests 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?" # base URL for the API
API_KEY = "950f313154000395ba6ce7f3c4d942cb" # API key for the API

# function to get the city name from the user
def get_city():
    print("Welcome to the Weather App")
    while True:
        city = input("Enter the city name: ")
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city
        response = requests.get(url).json()
        if response.get("cod") != 200:
            print("Please enter a valid city name")
        else:
            return city

# function to convert kelvin to celsius and farhenheit
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    farhenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, farhenheit



# getting the city name from the user and creating the URL
city = get_city()
url = BASE_URL + "appid=" + API_KEY + "&q=" + city

# getting the response from the API
response = requests.get(url).json()

# checking temperature unit
temp_kelvin = response['main']['temp']
temp_celsius, temp_farhenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

# checking feels like temperature unit
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_farhenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

# checking wind speed
wind_speed = response['wind']['speed']

# checking humidity
humidity = response['main']['humidity']

# checking weather description
description = response['weather'][0]['description']

# checking sunrise and sunset time
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'], dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'], dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

# printing the weather details
print("\n")
print(f"Temperature in {city}: {temp_celsius:.1f}°C or {temp_farhenheit:.2f}°F")
print(f"Temperature in {city} feels like: {feels_like_celsius:.1f}°C or {feels_like_farhenheit:.2f}°F")
print(f"Wind speed in {city}: {wind_speed} m/s")
print(f"Humidity in {city}: {humidity}%")
print(f"General Weather in {city}: {description.capitalize()}")
print(f"Sunrise time in {city}: {sunrise_time}")
print(f"Sunset time in {city}: {sunset_time}")
