import os

from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives import serialization
from symmetric_crypto import encrypt_data
from asymmetric_crypto import generate_key_pair, encrypt_symmetric_key, decrypt_symmetric_key
from serialization import serialize_private_key, serialize_public_key, load_private_key


def generate_keys(private_key_path, public_key_path, symmetric_key_path):
    try:
        private_key = generate_key_pair()
        public_key = private_key.public_key()
        symmetric_key = os.urandom(32)
        with open(public_key_path, "wb") as f:
            f.write(serialize_public_key(public_key))
        with open(private_key_path, "wb") as f:
            f.write(serialize_private_key(private_key))
        with open(symmetric_key_path, "wb") as f:
            f.write(symmetric_key)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def encrypt_file(initial_file_path, private_key_path, symmetric_key_path, encrypted_file_path):
    try:
        private_key_bytes = open(private_key_path, "rb").read()
        private_key = load_private_key(private_key_bytes)
        symmetric_key = open(symmetric_key_path, "rb").read()
        encrypted_symmetric_key = encrypt_symmetric_key(private_key, symmetric_key)
        with open(symmetric_key_path, "wb") as f:
            f.write(encrypted_symmetric_key)
        with open(initial_file_path, "rb") as f_in, open(encrypted_file_path, "wb") as f_out:
            plaintext = f_in.read()
            ciphertext = encrypt_data(symmetric_key, plaintext)
            f_out.write(ciphertext)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")
