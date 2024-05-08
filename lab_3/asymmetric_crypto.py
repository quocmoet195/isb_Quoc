from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_key_pair():
    try:
        return rsa.generate_private_key(public_exponent=65537, key_size=2048)
    except Exception as ex:
        raise Exception(f"ERROR!!{ex}")