import hashlib


def check_card_number(center_part: int, bins: list, last_four_numbers: int, original_hash: str) -> str:
    """
    Функция проверяет номер карты хешу соответствует или нет
    original_hash: Хеш карты
    last_four_numbers: Последние 4 цифры карты
    Return: Номер карты
    """
    for bin_part in bins:
        card_number = f"{bin_part}{str(center_part).zfill(6)}{last_four_numbers}"
        if hashlib.blake2b(card_number.encode()).hexdigest() == original_hash:
            return card_number
