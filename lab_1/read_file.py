def read_from_file(path: str) -> str:
    try:
        with open(path, "r+", encoding="utf-8") as file:
            data = file.read()
        return data
    except Exception:
       raise Exception("Failed to open file or file was not found!\n")

