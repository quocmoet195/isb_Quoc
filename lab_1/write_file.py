import logging


logging.basicConfig(level=logging.INFO)


def write_to_file(path: str, data: str) -> None:
    """
    Writes data to a file.
    Args:
        path (str): The path to the file.
        data (str): The data to be written to the file.
    Raises:
        IOError: If the file cannot be opened or written.
    """
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as ex:
        logging.error(f"Failed to write data or file was not found: {ex}\n")