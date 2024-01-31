# gui.py
import tkinter as tk
from api import get_weather
print(tk.TkVersion)
def fetch_weather():
    """
    Fetch weather data when the user clicks the "Fetch Weather" button.
    """
    # Get the location from the entry widget
    location = location_entry.get()

    try:
        # API key
        api_key = "your_api_key"
        
        # Fetch weather data using the API
        weather_data = get_weather(api_key, location)

        # Update the labels with the fetched weather data
        temperature_label.config(text=f"Temperature: {weather_data['temperature']}°C")
        humidity_label.config(text=f"Humidity: {weather_data['humidity']}%")
        conditions_label.config(text=f"Conditions: {weather_data['description']}")
    except Exception as e:
        # Display an error message if there's an issue
        error_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and pack labels
location_label = tk.Label(root, text="Enter location:")
location_label.pack(pady=10)

# Entry widget for location input
location_entry = tk.Entry(root)
location_entry.pack(pady=10)

# Button to fetch weather
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

# Labels to display weather information
temperature_label = tk.Label(root, text="")
temperature_label.pack(pady=10)

humidity_label = tk.Label(root, text="")
humidity_label.pack(pady=10)

conditions_label = tk.Label(root, text="")
conditions_label.pack(pady=10)

# Label for error messages
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
