# OIBSIP (Oasis Infobyte Tech Internship)

Welcome to the OIBSIP repository for the Oasis Infobyte Tech Internship! This repository contains the tasks and projects completed during the internship.

## Weather App

This Weather App allows users to fetch and display current weather data for a specified location using both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter.

## Features

- **CLI Version:**
  - User inputs the location (city or ZIP code) in the terminal.
  - Fetches and displays current temperature, humidity, and weather conditions.

- **GUI Version (Tkinter):**
  - User can input the location in a graphical interface.
  - Fetches and displays current temperature, humidity, and weather conditions.
  - GUI updates dynamically upon user interaction.

## Prerequisites

- Python 3.x
- Tkinter (for GUI)

## Setup

1. **Download the OIBSIP Repository:**
   - Download the OIBSIP repository from [https://github.com/CyberRide/OIBSIP](https://github.com/CyberRide/OIBSIP).

2. **Navigate to the Weather App Directory:**
   - Open the OIBSIP repository on your local machine.

3. **Install Required Dependencies:**
   - Open a terminal or command prompt and navigate to the "WeatherApp" directory inside the OIBSIP repository:

     ```bash
     cd WeatherApp
     ```

   - Install the required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

4. **Run the CLI Version:**
   - Run the CLI version of the Weather App:

     ```bash
     python main.py
     ```

5. **Run the GUI Version:**
   - Run the GUI version of the Weather App:

     ```bash
     python gui.py
     ```

## Configuration

- For the GUI version, replace `"your_api_key"` with your OpenWeatherMap API key in `gui.py` and `main.py` .


## License

This project is licensed under the [MIT License](LICENSE).
