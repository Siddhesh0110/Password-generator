import random
import string

def generate_password(length=12):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage
password = generate_password(16)
print("Generated Password:", password)
