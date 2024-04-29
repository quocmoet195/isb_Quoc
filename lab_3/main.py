import argparse
import json
import os
from generate_key import generate_key_pair
from encrypt import encrypt_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Hybrid encryption using an asymmetric and symmetric key")
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-gen', '--generation', action='store_true',help='Run key generation mode')
    mode_group.add_argument('-enc', '--encryption', action='store_true',help='Run encryption mode')
    mode_group.add_argument('-dec', '--decryption', action='store_true',help='Run decryption mode')
    args = parser.parse_args()
    SETTINGS_FILE = os.path.join('files', 'settings.json')
    try:
        with open(SETTINGS_FILE) as json_file:
            settings = json.load(json_file)
    except Exception as ex:
        raise Exception(f"Error loading settings file: {ex}")
    try:
        if args.generation:
            generate_key_pair(settings['private_key'], settings['public_key'], settings['symmetric_key'])
        if args.encryption:
            encrypt_data(settings['initial_file'], settings['private_key'], settings['symmetric_key'], settings['encrypted_file'])
    except Exception as ex:
        raise Exception(f"Error: {ex}")