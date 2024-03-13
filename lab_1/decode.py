import argparse
import json
import os
import read_file
import write_file


def get_dict(input_path: str, output_path: str) -> None:
    try:
        data = read_file.read_from_file(input_path)
        my_dict = {}

        for char in data:
            my_dict[char] = my_dict.get(char, 0) + 1

        total_chars = len(data)
        relative_freq_dict = {char: count / total_chars for char, count in my_dict.items()}

        sorted_dict = dict(sorted(relative_freq_dict.items(), key=lambda x: x[1], reverse=True))

        with open(output_path, "w", encoding="utf-8") as json_file:
            json.dump(sorted_dict, json_file, ensure_ascii=False, indent=1)

    except Exception as ex:
        raise Exception("Error when creat and save to dictionary!")


def decode_text(encrypted_text: str, key_path: str, decrypted_text: str) -> None:
    try:
        data = read_file.read_from_file(encrypted_text)

        with open(key_path, "r", encoding="utf-8") as key_file:
            dict = json.load(key_file)

        for key, value in dict.items():
            data = data.replace(key, value)

        write_file.write_to_file(decrypted_text, data)

    except Exception as ex:
        raise Exception("Error when decode text!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decryption of text encrypted with monoalphabetic substitution")
    abs_path = os.path.abspath("")
    parser.add_argument(
        "--input_file",
        type=str,
        default=os.path.join(abs_path,"part_2","cod1.txt"),
    )

    parser.add_argument(
        "--freq_dict",
        type=str,
        default=os.path.join(abs_path,"part_2","frep.json"),
    )

    parser.add_argument(
        "--key_dict",
        type=str,
        default=os.path.join(abs_path,"part_2","key.json"),
    )

    parser.add_argument(
        "--output_file",
        type=str,
        default=os.path.join(abs_path,"part_2","decoded_text.txt"),
    )

    args = parser.parse_args()

    try:
        get_dict(args.input_file,args.freq_dict)
        decode_text(args.input_file,args.key_dict,args.output_file)
        print("Text successfully decrypted and saved")
    except Exception as ex:
        raise Exception("Error when decode!")