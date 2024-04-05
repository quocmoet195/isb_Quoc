import json
from math import sqrt
from scipy.special import erfc
from scipy.special import gammaincc

pi = [0.2148, 0.3672, 0.2305, 0.1875]

def frequency_bit_test(bits:str)->float:
    """
    Проверить сгенерированные последовательность с помощью частотного побитового теста
    Argument:
        bits: Двоичных последовательностей
    Returns:
        P: Вероятность того, что генератор производит значения, сравнимые с эталоном.
    """
    bits_size=len(bits)
    count_one = bits.count('1')
    count_zero = bits.count('0')
    total = count_one - count_zero
    S = total/sqrt(bits_size)
    P = erfc(abs(S)/sqrt(2))
    print(P)
    if (P < 0.01):
        print("Failed test")
    else:
        print( "Passed test")
    return P


def consecutive_bits_test(bits:str)->float:
    """
    Проверить сгенерированные последовательность с помощью одинаковых подряда идущие биты.    
    Argument:
        bits: Двоичных последовательностей
    Returns:
        P: Вероятность того, что генератор производит значения, сравнимые с эталоном.
    """
    bits_size=len(bits)
    one_count = bits.count('1') 
    f1=one_count/bits_size
    if(abs(f1-0.5)<2/sqrt(bits_size)):
        count = 0
        for i in range (bits_size-1):
            if bits[i] != bits[i+1]:
                count+=1
        P = erfc(abs(count-2*bits_size*f1*(1-f1))/(2*sqrt(2*bits_size)*f1*(1-f1)))
    else:
        P=0;
    print(P)
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")
    return P


def longest_sequence_of_ones_test(bits:str)->float:
    """
    Проверить сгенерированные последовательность с помощью самой длинной последовательности единиц в блоке.    
    Argument:
        bits: Двоичных последовательностей
    Returns:
        P: Вероятность того, что генератор производит значения, сравнимые с эталоном.
    """
    M= len(bits)
    N=int(M/8)
    max_list = []
    for i in range(N):
        block = bits[i * 8: (i + 1) * 8]
        one_count = 0
        max_one_in_block = 0
        for bit in block:
            if bit == '1':
                one_count += 1
                max_one_in_block = max(max_one_in_block, one_count)
            else:
                one_count = 0
        max_list.append(max_one_in_block)
    v1 = max_list.count(0)+max_list.count(1)
    v2 = max_list.count(2)
    v3 = max_list.count(3)
    v4 = 16-v1-v2-v3
    X = ((v1-N*pi[0])**2)/(N*pi[0]) + ((v2-N*pi[1])**2)/(N*pi[1]) + ((v3-N*pi[2])**2)/(N*pi[2]) + ((v4-N*pi[3])**2)/(N*pi[3])
    P=gammaincc(3/2,X/2)
    print(P)
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")
    return P


def calculate(bits:str):
    P1 = frequency_bit_test(bits)
    P2 = consecutive_bits_test(bits)
    P3 = longest_sequence_of_ones_test(bits)
    return P1, P2, P3


if __name__ == "__main__":
    try:
        with open('settings.json','r') as file:
            bits_dict=json.load(file)
    except Exception as ex:
        raise Exception(f"Error when read bits!\n Exception{ex}")
    bits_cpp=str(bits_dict['bits_cpp'])
    bits_java=str(bits_dict['bits_java'])
    output_path=bits_dict['output_path']
    result_P1, result_P2, result_P3 = calculate(bits_cpp)
    try:
        with open(output_path,"w") as file:
            file.write('Test with the C++ random requense\n')
            file.write(json.dumps({"Frequency bit test":result_P1, "Consecutive bits test": result_P2, "Longest sequence of ones test": result_P3}, indent=1))
    except Exception as ex:
        raise Exception(f"Error when write into file!\n Exception{ex}")
    result_P1, result_P2, result_P3 = calculate(bits_java)
    try:
        with open(output_path,"a") as file:
            file.write('\n\nTest with the java random requense\n')
            file.write(json.dumps({"Frequency bit test":result_P1, "Consecutive bits test": result_P2, "Longest sequence of ones test": result_P3}, indent=1))
    except Exception as ex:
        raise Exception(f"Error when write into file!\n Exception{ex}")
