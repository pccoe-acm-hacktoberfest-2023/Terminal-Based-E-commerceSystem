from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('secure_storage/key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    return open('secure_storage/key.key', 'rb').read()


def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password)
