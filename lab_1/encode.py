import os
import read_file
import write_file

abs_path = os.path.abspath("")
alphabet_path=os.path.join(abs_path,"part_1","alphabet.txt")
ALPHABET=read_file.read_from_file(alphabet_path)

def encryption_text(input_path: str, output_path: str, step_path: str) -> None:
    try:
        step=int(read_file.read_from_file(step_path))
        data = read_file.read_from_file(input_path)
        data=data.lower()
        encrypted_data = ""
        for char in data:
            if char in ALPHABET:
                index = (ALPHABET.index(char) + step) % len(ALPHABET)
                encrypted_data += ALPHABET[index]
            else:
                encrypted_data += char
        write_file.write_to_file(output_path, encrypted_data)
    except Exception:
        raise Exception("Error when encode text!\n")  


if __name__ == "__main__":
    abs_path = os.path.abspath("")
    input_path=os.path.join(abs_path,"part_1","original_text.txt")
    output_path=os.path.join(abs_path,"part_1","encode_text.txt")
    step_path=os.path.join(abs_path,"part_1","step.txt")

    try:
        encryption_text(input_path, output_path, step_path)
        print("Text successfully encoded")
    except Exception:
        raise Exception("Error when encode!")