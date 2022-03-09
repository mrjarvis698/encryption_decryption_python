from cryptography.fernet import Fernet

def generate():
    key_generation = Fernet.generate_key()
    with open('Secret.key', 'wb') as mykey:
        mykey.write(key_generation)
    
    print("Secret Key :","'" + key_generation.decode() + "'")

if __name__ == "__main__":
    generate()
