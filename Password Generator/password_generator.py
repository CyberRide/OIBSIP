# password_generator.py

# Importing necessary modules
import random
import string

# Function to generate a random password based on user-defined criteria
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    
    # Building the character set based on user preferences
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Checking if at least one character set is selected
    if not characters:
        raise ValueError("At least one character set (letters, numbers, symbols) must be selected.")
    
    # Generating the password using the selected character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Function to validate user input for password generation
def validate_input(length, use_letters, use_numbers, use_symbols):
    # Checking if password length is a positive integer
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Password length must be a positive integer.")
    
    # Checking if at least one character set is selected
    if not any([use_letters, use_numbers, use_symbols]):
        raise ValueError("At least one character set (letters, numbers, symbols) must be selected.")


# Main function to run the password generation process
def main():
    try:
        # Getting user input for password criteria
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Validating user input
        validate_input(length, use_letters, use_numbers, use_symbols)
        
        # Generating the password and printing it
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")

    except ValueError as e:
        # Handling potential errors and displaying error messages
        print(f"Error: {e}")
        

# Running the main function if the script is executed directly
if __name__ == "__main__":
    main()
