import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding


def encrypt_data(symmetric_key, plaintext):
    try:
        iv = os.urandom(16)
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None) 
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return iv + ciphertext
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def decrypt_data(symmetric_key, ciphertext, iv):
    try:
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")
