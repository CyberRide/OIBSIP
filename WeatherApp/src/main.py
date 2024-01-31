# main.py
from api import get_weather
# from gui import run_gui
from utils import validate_location, display_error_message

def main():
    try:
        # Get user input for location
        location = input("Enter location (city or ZIP code): ")

        # Validate the user-provided location
        validate_location(location)

        #OpenWeatherMap API key
        api_key = "your_api_key"

        # Fetch weather data using the API
        weather_data = get_weather(api_key, location)

        # Display weather information in the console
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Conditions: {weather_data['description']}")

        # Uncomment the next line to run the GUI
        #run_gui(weather_data)

    except Exception as e:
        display_error_message(str(e))

if __name__ == "__main__":
    main()
