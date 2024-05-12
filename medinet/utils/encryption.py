import rsa
import pycryptodome as cryptodome

def generate_keys(key_size):
    # Generate RSA keys
    return rsa.newkeys(key_size)

def encrypt_data(data, public_key):
    # Encrypt data with RSA
    return rsa.encrypt(data, public_key)

def decrypt_data(encrypted_data, private_key):
    # Decrypt data with RSA
    return rsa.decrypt(encrypted_data, private_key).decode()

def aes_encrypt(data, key):
    # Encrypt data with AES
    cipher = cryptodome.Cipher.new(cryptodome.AES.MODE_EAX, key)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return ciphertext, tag, cipher.nonce

def aes_decrypt(encrypted_data, tag, key, nonce):
    # Decrypt data with AES
    cipher = cryptodome.Cipher.new(cryptodome.AES.MODE_EAX, key, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(encrypted_data, tag)
    return plaintext.decode()
