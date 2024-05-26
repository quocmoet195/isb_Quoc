import hashlib
import multiprocessing as mp


def check_card_number(args) -> str:
    """
    Checks if a card number matches the original hash.
    args: Tuple containing center_part, bins, last_four_numbers, original_hash
    """
    center_part, bins, last_four_numbers, original_hash = args
    for bin_part in bins:
        card_number = f"{bin_part}{str(center_part).zfill(6)}{last_four_numbers}"
        if hashlib.blake2b(card_number.encode()).hexdigest() == original_hash:
            return card_number
    return None

def create_card_number(original_hash: str, bins: list, last_four_numbers: str, core_number: int = mp.cpu_count()) -> str:
    """
    Generates the card number by comparing hashes.
    original_hash: Original hash of the card
    bins: List of BINs (Bank Identification Numbers)
    last_four_numbers: Last four digits of the card number
    core_number: Number of CPU cores to use for multiprocessing
    """
    with mp.Pool(core_number) as pool:
        args = [(i, bins, last_four_numbers, original_hash) for i in range(0, 1000000)]
        results = pool.map(check_card_number, args)
        for result in results:
            if result:
                pool.terminate() 
                return result
    return None
