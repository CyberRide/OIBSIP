# utils.py
import re

def validate_location(location):
    """
    Validate the user-provided location.

    Args:
        location (str): The location entered by the user.

    Raises:
        ValueError: If the location is empty or contains invalid characters.
    """
    if not location:
        raise ValueError("Location cannot be empty.")
    
    # Check if the location contains only letters, digits, or spaces
    if not re.match(r"^[a-zA-Z0-9\s]*$", location):
        raise ValueError("Invalid characters in the location. Please use letters, digits, or spaces.")

def display_error_message(message):
    """
    Display an error message.

    Args:
        message (str): The error message to display.
    """
    print(f"Error: {message}")
