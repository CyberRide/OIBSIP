# gui.py
# Author: CyberRide
# GitHub: https://github.com/CyberRide/
import os
import tkinter as tk
from api import get_weather
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim

def get_current_location():
    """
    Get the user's current location based on their IP address.
    """
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode('')
        if location:
            return f"{location.latitude},{location.longitude}"
    except Exception as e:
        print(f"Error getting current location: {str(e)}")
    return None

def fetch_weather():
    """
    Fetch weather data when the user clicks the "Fetch Weather" button.
    """
    # Get the location from the entry widget or use the current location
    location = location_entry.get() or get_current_location()

    if not location:
        error_label.config(text="Unable to determine the location.")
        return

    try:
        # Show loading animation while waiting for API response
        loading_label.config(text="Fetching data...")
        root.update()

        # API key
        api_key = "Your Api Key"
        
        # Fetch weather data using the API
        weather_data = get_weather(api_key, location)

        # Update the temperature label with the fetched weather data and resized icon
        temperature_label.config(text=f"Temperature: {weather_data['temperature']}°C")
        show_icon('temperature.gif', temperature_icon_label, width=30, height=30)

        # Update the humidity label with the fetched weather data and resized icon
        humidity_label.config(text=f"Humidity: {weather_data['humidity']}%")
        show_icon('humidity.gif', humidity_icon_label, width=30, height=30)

        # Update the conditions label with the fetched weather data and static icon
        conditions_label.config(text=f"Conditions: {weather_data['description']}")
        show_icon('default.gif', conditions_icon_label, width=30, height=30)
        
        # Clear error message
        error_label.config(text="")
    except Exception as e:
        # Display an error message if there's an issue
        error_label.config(text=f"Error: {str(e)}")
    finally:
        # Hide loading animation
        loading_label.config(text="")

def show_icon(icon_path, icon_label, width, height):
    """
    Show an animated icon based on the given path.
    """
    image = Image.open(icon_path)
    animated_icon = ImageTk.PhotoImage(image)

    icon_label.config(image=animated_icon)
    icon_label.image = animated_icon
# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and pack labels
bold_font = (None, 10, "bold")

location_label = tk.Label(root, text="Enter location or leave blank for current location:", font=bold_font)
location_label.grid(row=0, column=0, columnspan=3, pady=10, sticky='w')

# Entry widget for location input
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=0, columnspan=3, pady=10, sticky='we')

# Button to fetch weather
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.grid(row=2, column=0, columnspan=3, pady=10)

# Loading label for animation
loading_label = tk.Label(root, text="")
loading_label.grid(row=3, column=0, columnspan=3, pady=10)

# Temperature label with animated icon
temperature_label = tk.Label(root, text="")
temperature_label.grid(row=4, column=0, pady=10)

temperature_icon_label = tk.Label(root, text="")
temperature_icon_label.grid(row=4, column=1, pady=10)

# Humidity label with animated icon
humidity_label = tk.Label(root, text="")
humidity_label.grid(row=5, column=0, pady=10)

humidity_icon_label = tk.Label(root, text="")
humidity_icon_label.grid(row=5, column=1, pady=10)

# Conditions label with animated icon
conditions_label = tk.Label(root, text="")
conditions_label.grid(row=6, column=0, pady=10)

conditions_icon_label = tk.Label(root, text="")
conditions_icon_label.grid(row=6, column=1, pady=10)

# Label for error messages
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=7, column=0, columnspan=3, pady=10)


# Run the Tkinter main loop
root.mainloop()
