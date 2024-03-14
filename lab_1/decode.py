import json
import os
import read_file
import write_file


def get_dict(input_path: str, output_path: str) -> None:
    try:
        data = read_file.read_from_file(input_path)
        my_dict = {}
        freq_dict={}
        for char in data:
            if char in my_dict:
                my_dict[char] = (int(my_dict.get(char)) + 1) 
            else:
                my_dict[char] =  1
        total_chars = len(data)
        for key, val in my_dict.items():
            freq_dict[key]=val/total_chars
        sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
        with open(output_path,"w") as freq_file:
            freq_file.write(json.dumps(sorted_dict,indent=1,ensure_ascii=False))
    except Exception:
        raise Exception("Error when creat and save to dictionary!")

def decode_text(original_text: str, key_path: str, decode_text: str) -> None:
    try:
        data = read_file.read_from_file(original_text)
        with open(key_path, "r", encoding="utf-8") as key_file:
            key_dict = json.load(key_file)
        for key, value in key_dict.items():
            if key in data:
                data = data.replace(key, value)
        write_file.write_to_file(decode_text, data)
    except Exception:
        raise Exception("Error when decode text!")


if __name__ == "__main__":
    abs_path = os.path.abspath("")
    input_file=os.path.join(abs_path,"part_2","cod1.txt")
    freq_dict=os.path.join(abs_path,"part_2","frep.json")
    key_dict=os.path.join(abs_path,"part_2","key.json")
    output_file=os.path.join(abs_path,"part_2","decoded_text.txt")
    try:
        get_dict(input_file,freq_dict)
        decode_text(input_file,key_dict,output_file)
        print("Text successfully decrypted and saved")
    except Exception as ex:
        raise Exception("Error when decode!")