from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_key_pair():
    try:
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def encrypt_symmetric_key(private_key, symmetric_key):
    try:
        encrypted_key = private_key.public_key().encrypt(symmetric_key, 
                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                                                 algorithm=hashes.SHA256(), label=None))
        return encrypted_key                                                                      
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def decrypt_symmetric_key(private_key, encrypted_symmetric_key):
    try:
        return private_key.decrypt(encrypted_symmetric_key, asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        ))
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")