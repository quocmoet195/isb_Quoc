from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def serialize_private_key(private_key):
    try:
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def serialize_public_key(public_key):
    try:
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")

  
def load_private_key(private_key_bytes):
    try:
        return serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")


def load_public_key(public_key_bytes):
    try:
        return serialization.load_pem_public_key(public_key_bytes)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")
