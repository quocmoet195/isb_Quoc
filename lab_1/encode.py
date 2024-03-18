import os
from read_and_write_file import read_from_file, write_to_file

abs_path = os.path.abspath("")
alphabet_path=os.path.join(abs_path,"part_1","alphabet.txt")
ALPHABET=read_from_file(alphabet_path)

def encryption_text(input_path: str, output_path: str, step_path: str) -> None:
    """
    Расшифровать текст
    Arguments:
        input_path: Путь к файлу, содержащему исходный текст, который нужно зашифровать. Тип str.
        output_path: Путь к файлу, в котором содержит зашифрованный текст. Тип str.
        key_path: ключ зашифровки. Тип str.
    Return:
        None
    """
    try:
        step=int(read_from_file(step_path))
        data = read_from_file(input_path)
        data=data.lower()
        encrypted_data = ""
        for char in data:
            if char in ALPHABET:
                index = (ALPHABET.index(char) + step) % len(ALPHABET)
                encrypted_data += ALPHABET[index]
            else:
                encrypted_data += char
        write_to_file(output_path, encrypted_data)
    except Exception as ex:
        raise Exception(f"Error when encode text!\n Exception:{ex}\n")  


if __name__ == "__main__":
    abs_path = os.path.abspath("")
    input_path=os.path.join(abs_path,"part_1","original_text.txt")
    output_path=os.path.join(abs_path,"part_1","encode_text.txt")
    step_path=os.path.join(abs_path,"part_1","step.txt")

    try:
        encryption_text(input_path, output_path, step_path)
        print("Text successfully encoded")
    except Exception as ex:
        raise Exception(f"Error when encode!\n Exception:{ex}\n")