from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.backends import default_backend


def decrypt_data(encrypted_file_path: str, private_key_path: str, encrypted_symmetric_key_path: str,
                 decrypted_file_path: str) -> None:
    try:
        with open(encrypted_symmetric_key_path, "rb") as f1, open(private_key_path, "rb") as f2:
            encrypted_symmetric_key = f1.read()
            private_key_bytes = f2.read()
        private_key = serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())
        symmetric_key = private_key.decrypt(encrypted_symmetric_key, 
                                            asymmetric_padding.OAEP(mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()), 
                                                                    algorithm=hashes.SHA256(), 
                                                                    label=None
                                                                    )
                                            )
    except Exception as ex:
        raise Exception(f"{ex} not found")
    try:
        with open(encrypted_file_path, "rb") as f_in, open(decrypted_file_path, "wb") as f_out:
            iv = f_in.read(16)
            cipher = Cipher(algorithms.ChaCha20(symmetric_key, iv), mode=None)
            decryptor = cipher.decryptor()
            while chunk := f_in.read(128):
                decrypted_chunk = decryptor.update(chunk)
                f_out.write(decrypted_chunk)
            f_out.write(decryptor.finalize())
    except Exception as ex:
        raise Exception(f"{ex} not found")
