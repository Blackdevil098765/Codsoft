import random
import string

def generate_password():
    print("--- Password Generator ---")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("Security Note: Passwords shorter than 4 characters are weak.")
        characters = string.ascii_letters + string.digits + string.punctuation
        password_list = random.choices(characters, k=length)
        password = "".join(password_list)
        print(f"\nYour Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a numerical value for the length.")
if __name__ == "__main__":
    generate_password()
