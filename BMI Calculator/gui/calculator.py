# gui/calculator.py
# Author: CyberRide
# GitHub: https://github.com/CyberRide/

import tkinter as tk
from tkinter import messagebox
from utils.validation import validate_numeric_input
from utils.data_mgmt import save_bmi_data

# Function to calculate BMI based on weight and height
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to classify BMI into health categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Callback function for the "Calculate BMI" button
def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        # Display an error message for non-numeric inputs
        messagebox.showerror("Invalid Input", "Please enter numeric values for weight and height.")
        return

    if not validate_numeric_input(weight, height):
        # Display an error message for non-positive values
        messagebox.showerror("Invalid Input", "Weight and height must be positive values.")
        return

    # Calculate BMI and classify into categories
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    # Display the calculated BMI and health category
    result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")

    # Save BMI data to users.json
    save_bmi_data(weight, height, bmi, category)

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

# Weight Entry
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Height Entry
height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate BMI", command=on_calculate)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Display
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
