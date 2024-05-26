import hashlib
import multiprocessing as mp


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

def create_card_number(original_hash: str, bins: list, last_four_numbers: str, core_number: int = mp.cpu_count()) -> str:
    """
    Функция подбираем номер карты
    original_hash: Хеш карты
    bins: набор БИНов карты
    last_four_numbers: Последние 4 цифры карты
    core_number: Количество ядер
    Return: Номер карты
    """
    with mp.Pool(core_number) as p:
        args = [(i, bins, last_four_numbers, original_hash) for i in range(0, 999999)]
        for result in p.starmap(check_card_number, args):
            if result:
                p.terminate() 
                return result
