from cryptography.fernet import Fernet

def load_key():
    global key
    """
    Load the previously generated key
    """
    key = "jUejSkqUa9RoJW-ugGpGQFxvIHEW9o0f_pMqXdY2HN8="

def encrypt_message(message):
    """
    Encrypts a message
    """
    load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message).decode()
    print("Encryption:", "'" + encrypted_message + "'")
    
if __name__ == "__main__":
    encrypt_message(input("Enter Text to Encrypt: "))
