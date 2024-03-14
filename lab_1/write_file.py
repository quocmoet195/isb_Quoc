def write_to_file(path: str, data: str) -> None:
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception:
        raise Exception("Failed to write data or file was not found!\n")