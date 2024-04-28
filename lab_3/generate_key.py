import os
from cryptography.hazmat.primitives import hashes, padding, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def generate_key_pair(private_key_path: str,  public_key_path: str, symmetric_key_path: str) -> None:
    """Эта функция генерирует пару ключей(ассиметричный и симметричный) гибридной системы, а после сохраняет их в файлы.
    Args:
        private_key_path (str): путь до секретного ключа
        public_key_path (str): путь до общедоступного ключа
        symmetric_key_path (str): путь до симметричного ключа
    """
    #Генерация ключа для симметричного алгоритма
    symmetric_key = os.urandom(32)  # 256 бит = 32 байта
    #Генерация ключей для ассиметричного алгоритма
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    #Сериализация ассиметричных ключей
    try:
        with open(public_key_path, 'wb') as f_p, open(private_key_path, 'wb') as f_c:
            f_p.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                              format=serialization.PublicFormat.SubjectPublicKeyInfo))
            f_c.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                encryption_algorithm=serialization.NoEncryption()))
    except Exception as ex:
        raise Exception(f"{ex} not found")
    #Зашифрование ключа симметричного шифрования открытым ключом
    ciphertext = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(
        algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    try:
        with open(symmetric_key_path, "wb") as f:
            f.write(ciphertext)
    except Exception as ex:
        raise Exception(f"{ex} not found")
