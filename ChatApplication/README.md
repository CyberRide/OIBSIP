# OIBSIP (Oasis Infobyte Tech Internship)

Welcome to the OIBSIP repository for the Oasis Infobyte Tech Internship! This repository contains the tasks and projects completed during the internship.

## Chat Application

This Chat Application project provides both a basic text-based version for beginners and an advanced version with a graphical user interface (GUI) for more features.

## Features

- **Beginners Version:**
  - Command-line interface for real-time messaging.
  - Basic client-server model for message exchange.

- **Advanced Version (GUI):**
  - Graphical User Interface (GUI) using Tkinter/PyQt/web framework.
  - User authentication and registration.
  - Multiple chat rooms support.
  - Multimedia sharing (images, videos).
  - Message history storage and display.
  - Notifications for new messages.
  - Emoji support within messages.
  - Data security through encryption.

## Prerequisites

- Python 3.x
- Tkinter/PyQt (for GUI)
- Other dependencies listed in `requirements.txt`

## Setup Instructions

1. **Download the OIBSIP Repository:**
   - Download the OIBSIP repository from [https://github.com/CyberRide/OIBSIP](https://github.com/CyberRide/OIBSIP).

2. **Navigate to the Chat Application Directory:**
   - Open the OIBSIP repository on your local machine.

3. **Install Required Dependencies:**
   - Open a terminal or command prompt and navigate to the "ChatApplication" directory:

     ```bash
     cd ChatApplication
     ```

   - Install the required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Beginners Version (Command Line):**
   - Run the beginners version of the Chat Application:

     ```bash
     python server.py
     ```

     Open another terminal twice:
     ```bash
     python client.py
     ```

5. **Run the Advanced Version (GUI):**
   - Run the advanced version of the Chat Application:

     ```bash
     cd advanced_version
     python gui.py
     ```

## Configuration

- For the GUI version, replace placeholders such as API keys or other sensitive information in relevant files.

## License

This project is licensed under the [MIT License](LICENSE).
