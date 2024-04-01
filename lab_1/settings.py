import json

def path_settings(input_path)->str:
    """
    Все пути к файлам нужно проработать во 1 части.
    Arguments:
        None.
    Returns:
        input_path: Путь к файлу, содержащему исходный текст, который нужно зашифровать.
        output_path: Путь к файлу, в котором содержит зашифрованный текст.
        step_path: Путь к файлу, в котором содержит ключ зашифровки.
        alphabet_path: Путь к файлу, в котором содержит символы
    """
    try:
        with open(input_path,'r') as file:
            settings_path=json.load(file)
    except Exception as ex:
        raise Exception(f"Error when read path from file!\n Exception:{ex}\n")
    list_path=list(settings_path.values())
    
    return list_path[0], list_path[1], list_path[2], list_path[3]
