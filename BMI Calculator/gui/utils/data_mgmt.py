# utils/data_mgmt.py
# Author: CyberRide
# GitHub: https://github.com/CyberRide/

import os
import json
from datetime import datetime

def save_bmi_data(weight, height, bmi, category):
    """
    Saves BMI data to users.json.

    Parameters:
    - weight (float): The weight input.
    - height (float): The height input.
    - bmi (float): The calculated BMI.
    - category (str): The health category.

    Returns:
    - None
    """
    data_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "weight": weight,
        "height": height,
        "bmi": bmi,
        "category": category
    }

    # Ensure the 'data' directory exists
    os.makedirs("data", exist_ok=True)

    try:
        with open("data/users.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(data_entry)

    with open("data/users.json", "w") as file:
        json.dump(data, file, indent=2)
