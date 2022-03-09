from cryptography.fernet import Fernet

def load_key():
    global key
    """
    Load the previously generated key
    """
    key = "jUejSkqUa9RoJW-ugGpGQFxvIHEW9o0f_pMqXdY2HN8="

def decrypt_message(message):
    """
    Decrypts an encrypted message
    """
    load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(message)
    print("Decryption:","'" + decrypted_message.decode() + "'")

if __name__ == "__main__":
    decrypt_message(bytes(input("Enter Text to Encrypt: ").encode("UTF-8")))
