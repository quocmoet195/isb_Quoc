from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os


def encrypt_data(initial_file_path: str, private_key_path: str, encrypted_symmetric_key_path: str, encrypted_file_path: str) -> None:
    """Эта функция шифрует данные используя симметричный и ассиметричные ключи, а так же сохраняет результат по указыному пути
    Args:
        initial_file_path (str): путь до шифруемых данных
        private_key_path (str): путь до приватного ключа
        encrypted_symmetric_key_path (str): путь до зашифрованного симметричного ключа
        encrypted_file_path (str): путь куда шифруются данных
    """
    try:
        with open(private_key_path, "rb") as private_key_file:
            private_key = serialization.load_pem_private_key(
                private_key_file.read(),
                password=None,
                backend=default_backend()
            )
        symmetric_key = os.urandom(32)
        encrypted_symmetric_key = private_key.public_key().encrypt(
            symmetric_key,
            asymmetric_padding.OAEP(
                mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        with open(encrypted_symmetric_key_path, "wb") as encrypted_symmetric_key_file:
            encrypted_symmetric_key_file.write(encrypted_symmetric_key)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None) 
        encryptor = cipher.encryptor()
        with open(initial_file_path, "rb") as f_in, open(encrypted_file_path, "wb") as f_out:
            f_out.write(iv)
            while chunk := f_in.read(128):
                encrypted_chunk = encryptor.update(chunk)
                f_out.write(encrypted_chunk)
            f_out.write(encryptor.finalize())
    except Exception as ex:
        raise Exception(f"{ex} not found")
