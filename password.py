import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    # Create character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each character set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the remaining characters randomly from the combination of all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to avoid predictable sequences
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)

def main():
    try:
        size = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        
        # Generate the specified number of passwords
        passwords = [generate_password(size) for _ in range(num_passwords)]
        
        # Print each generated password
        for i, password in enumerate(passwords, 1):
            print(f"Password {i}: {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
