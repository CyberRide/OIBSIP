# utils/validation.py
# Author: CyberRide
# GitHub: https://github.com/CyberRide/

def validate_numeric_input(weight, height):
    """
    Validates if weight and height are numeric and positive.

    Parameters:
    - weight (float): The weight input.
    - height (float): The height input.

    Returns:
    - bool: True if both inputs are numeric and positive, False otherwise.
    """
    return weight > 0 and height > 0
