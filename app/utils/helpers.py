import base64
import os
import hashlib
import hmac
from cryptography.fernet import Fernet

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def generate_hmac(data, key):
    return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()

def generate_salt():
    return os.urandom(32)

def generate_password_hash(password, salt):
    return hashlib.sha256(password.encode() + salt).hexdigest()

def generate_fernet_key():
    return Fernet.generate_key()

def encrypt_data(data, fernet_key):
    fernet = Fernet(fernet_key)
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data, fernet_key):
    fernet = Fernet(fernet_key)
    return fernet.decrypt(encrypted_data.encode()).decode()

def generate_base64_encoded_hash(data):
    return base64.b64encode(generate_hash(data).encode()).decode()

def generate_base64_encoded_hmac(data, key):
    return base64.b64encode(generate_hmac(data, key).encode()).decode()

def generate_base64_encoded_salt():
    return base64.b64encode(generate_salt()).decode()

def generate_base64_encoded_password_hash(password, salt):
    return base64.b64encode(generate_password_hash(password, salt).encode()).decode()

def generate_base64_encoded_fernet_key():
    return base64.b64encode(generate_fernet_key()).decode()

def generate_base64_encoded_encrypted_data(data, fernet_key):
    return base64.b64encode(encrypt_data(data, fernet_key).encode()).decode()

def generate_base64_encoded_decrypted_data(encrypted_data, fernet_key):
    return decrypt_data(base64.b64decode(encrypted_data.encode()), fernet_key).decode()
