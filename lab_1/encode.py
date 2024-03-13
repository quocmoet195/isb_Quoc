import argparse
import os
import read_file
import write_file




ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
SYMBOLS = " ,.-;()?!+"


def encryption_text(path: str, encode_path: str, step: int) -> None:
    try:
        data = read_file.read_from_file(path)
        data=data.lower()
        result = "".join(char if char in SYMBOLS else ALPHABET[(ALPHABET.find(char) + step) % len(ALPHABET)] for char in data)

        write_file.write_to_file(encode_path, result)
    except Exception:
        raise Exception("Error when encode text!!!\n")  


if __name__ == "__main__":
    full_path = os.path.abspath("")
    parser = argparse.ArgumentParser() 
    parser.add_argument(
        "--input_file",
        type=str,
        default=os.path.join(full_path,"part_1","original_text.txt")
        
    )
    
    parser.add_argument(
        "--output_file",
        type=str,
        default=os.path.join(full_path,"part_1","encode_text.txt"),
    )

    parser.add_argument(
        "--step",
        type=int,
        default=1,
    )

    args = parser.parse_args()

    try:
        encryption_text(args.input_file, args.output_file, args.step)
        print("Text successfully encoded")
    except Exception as exception:
        raise Exception("Error when encode!!!")