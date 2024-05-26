import json
import argparse

from card import create_card_number
from measure_time import mark_global_point , load_statistics, measure_time
from luhn import Luhn


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-card', '--card_number_enumeration', type=int, nargs='?', const=6,
                       help='Ищет номер карты с помощью хеша')
    group.add_argument('-sta', '--statistics', action='store_true',
                       help='Получается статистику подбирая номер карты на разном количестве процессов')
    group.add_argument('-lun', '--lunh_algorithm', action='store_true',
                       help='Проверяет валидность номера карты с помощью алгоритма Луна')
    group.add_argument('-vis', '--visualize_statistics', action='store_true',
                       help='Создает гистограмму по имеющейся статистике')
    args = parser.parse_args()
    try:
        with open("settings.json", "r", encoding='UTF-8') as f:
            settings = json.load(f)
    except Exception as ex:
        raise Exception(f"Не удалось считать данные!{ex}")
    
    hash_number = settings['hash']
    bins = settings['bins']
    last_four_numbers = settings['last_four_numbers']
    card_file=settings['card_number']
    file_statistic=settings['file_statistics']
    png_file=settings['image_statistics']
    if args.card_number_enumeration:
        card_number = create_card_number(hash_number, bins, last_four_numbers, 6)
        if card_number:
            print(f"Номер карты успешно найден: {card_number}")
            with open(card_file, 'w') as f:
                f.write(card_number)
        else:
            print("Не удалось найти номер карты")
    elif args.statistics:
        measure_time(hash_number, bins, last_four_numbers, file_statistic)
    elif args.lunh_algorithm:
        with open(card_file, 'r') as f:
            card_number = f.read()
        if Luhn(card_number):
            print("Номер карты действителен")
        else:
            print("Номер карты не действителен")
    elif args.visualize_statistics:
        mark_global_point(load_statistics(file_statistic), png_file)
        print("Гистограмма успешно создана")
