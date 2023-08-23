import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(char) for _ in range(length))
    
    return password

password_length = int(input("Enter Your Desired Password Length: "))
Generated_password = generate_password(password_length)
print("Your Generated Password Is:", Generated_password)