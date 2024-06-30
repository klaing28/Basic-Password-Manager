
import os
import json
from cryptography.fernet import Fernet

#Key stuff
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    return open("key.key", "rb").read()

if not os.path.exists("key.key"):
    generate_key()

# Encrypt and decrypt
def encrypt(password):
    enc_password = cipher_suite.encrypt(password.encode())
    return enc_password

def decrypt(enc_password):
    dec_password = cipher_suite.decrypt(enc_password).decode()
    return dec_password

# Json wr
def load(filename="psw.json"):
    try:
        with open(filename, "r") as file:
            passwords = json.load(file)
        return passwords
    except FileNotFoundError:
        return {}

def save(passwords, filename="psw.json"):
    with open(filename, "w") as file:
        json.dump(passwords, file)



# Add, get, print
def add(service, password):
    enc_password = encrypt(password)
    passwords[service] = enc_password.decode()  # Store as string
    save(passwords)

def get(service):
    if service in passwords:
        enc_password = passwords[service].encode()  # Convert back to bytes
        return decrypt(enc_password)
    else:
        return None


def print_service():
    if passwords:
        print("Services stored:")
        for service in passwords:
            print(service)
    else:
        print("No services stored.")



key = load_key()
cipher_suite = Fernet(key)
passwords = load()

def main():

    while True:
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Print services")
        print("4. Change entrance password")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            add(service, password)
            print("Password added successfully!")
        elif choice == "2":
            service = input("Enter the service name: ")
            password = get(service)
            if password:
                print(f"The password for {service} is {password}")
            else:
                print("No password found for this service.")
        elif choice == "3":
            print_service()
        elif choice == "4":
            change_entrance_password()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

        print("\n")


if __name__ == "__main__":
    main()