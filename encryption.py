from cryptography.fernet import Fernet

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = "jUejSkqUa9RoJW-ugGpGQFxvIHEW9o0f_pMqXdY2HN8="
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    print("Encryption: ", encrypted_message)
    

if __name__ == "__main__":
    encrypt_message(input("Enter Text to Encrypt: "))