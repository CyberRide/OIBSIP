# api.py
# Author: CyberRide
# GitHub: https://github.com/CyberRide/
import requests

print(requests.__version__)
def get_weather(api_key, location):
    # Define the base URL for the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Set parameters for the API request, including the location, API key, and unit preference
    params = {"q": location, "appid": api_key, "units": "metric"}  # Use "imperial" for Fahrenheit
    
    # Make a GET request to the OpenWeatherMap API
    response = requests.get(base_url, params=params, timeout=60)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract relevant weather data
        weather_data = response.json()
        
        # Return the parsed weather data
        return parse_weather_data(weather_data)
    else:
        # Raise an exception if there was an error fetching weather data
        raise Exception(f"Error fetching weather data: {response.status_code}")

def parse_weather_data(data):
    # Extract relevant information from the JSON response
    main_data = data["main"]
    weather_conditions = data["weather"][0]

    # Create a dictionary with the parsed weather data
    parsed_data = {
        "temperature": main_data["temp"],
        "humidity": main_data["humidity"],
        "description": weather_conditions["description"],
    }

    # Return the dictionary containing the parsed weather data
    return parsed_data
