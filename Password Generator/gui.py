# gui.py

import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

class AdvancedPasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Password Generator")

        # Variables to store user input
        self.length_var = tk.StringVar(value="12")  # Default length
        self.use_letters_var = tk.BooleanVar(value=True)
        self.use_numbers_var = tk.BooleanVar(value=True)
        self.use_symbols_var = tk.BooleanVar(value=True)
        self.complexity_var = tk.StringVar(value="Medium")  # Default complexity

        # GUI elements
        self.create_gui()

    def create_gui(self):
        # Password length
        length_label = tk.Label(self.master, text="Password Length:")
        length_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        length_entry = tk.Entry(self.master, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, padx=10, pady=5)

        # Character sets checkboxes
        letters_checkbox = tk.Checkbutton(self.master, text="Include Letters", variable=self.use_letters_var)
        letters_checkbox.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        numbers_checkbox = tk.Checkbutton(self.master, text="Include Numbers", variable=self.use_numbers_var)
        numbers_checkbox.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        symbols_checkbox = tk.Checkbutton(self.master, text="Include Symbols", variable=self.use_symbols_var)
        symbols_checkbox.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        # Password complexity
        complexity_label = tk.Label(self.master, text="Password Complexity:")
        complexity_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        complexity_options = ["Low", "Medium", "High"]
        complexity_menu = tk.OptionMenu(self.master, self.complexity_var, *complexity_options)
        complexity_menu.grid(row=4, column=1, padx=10, pady=5)

        # Generate and Copy buttons
        generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        copy_button = tk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.grid(row=6, column=0, columnspan=2, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            use_letters = self.use_letters_var.get()
            use_numbers = self.use_numbers_var.get()
            use_symbols = self.use_symbols_var.get()

            # Validate user input
            self.validate_input(length, use_letters, use_numbers, use_symbols)

            # Generate password based on complexity
            password = self.generate_complex_password(length, use_letters, use_numbers, use_symbols)
            
            # Display the generated password
            messagebox.showinfo("Generated Password", f"Generated Password: {password}")

        except ValueError as e:
            # Handle potential errors and display error messages
            messagebox.showerror("Error", f"{e}")

    def generate_complex_password(self, length, use_letters, use_numbers, use_symbols):
        # Define character sets based on user preferences
        letters = string.ascii_letters if use_letters else ''
        numbers = string.digits if use_numbers else ''
        symbols = string.punctuation if use_symbols else ''

        # Ensure at least one character set is selected
        if not any([letters, numbers, symbols]):
            raise ValueError("At least one character set (letters, numbers, symbols) must be selected.")

        # Password complexity rules
        if self.complexity_var.get() == "Low":
            return ''.join(random.choice(letters + numbers + symbols) for _ in range(length))
        elif self.complexity_var.get() == "Medium":
            return ''.join(random.choice(letters + numbers + symbols) for _ in range(length // 2)) + \
                   ''.join(random.choice(letters) for _ in range(length // 4)) + \
                   ''.join(random.choice(numbers) for _ in range(length // 4))
        else:  # High complexity
            return ''.join(random.choice(letters) for _ in range(length // 3)) + \
                   ''.join(random.choice(numbers) for _ in range(length // 3)) + \
                   ''.join(random.choice(symbols) for _ in range(length // 3))

    def validate_input(self, length, use_letters, use_numbers, use_symbols):
        # Validate password length
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Password length must be a positive integer.")

        # Validate at least one character set is selected
        if not any([use_letters, use_numbers, use_symbols]):
            raise ValueError("At least one character set (letters, numbers, symbols) must be selected.")

    def copy_to_clipboard(self):
        # Copy the generated password to the clipboard
        password = self.generate_complex_password(
            int(self.length_var.get()),
            self.use_letters_var.get(),
            self.use_numbers_var.get(),
            self.use_symbols_var.get()
        )
        pyperclip.copy(password)
        messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard!")

# Creating the main GUI window
root = tk.Tk()
app = AdvancedPasswordGenerator(root)
root.mainloop()
