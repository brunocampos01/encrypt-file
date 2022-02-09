import argparse
import time

from encryptfile.encryptfile import decrypt_file
from encryptfile.encryptfile import encrypt_file
from encryptfile.encryptfile import open_file
from humanfriendly import format_timespan
from pyfiglet import Figlet

f = Figlet(font='slant')


def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files with ONLY ONE COMMAND')
    parser.add_argument('--func',
                        type=str,
                        required=True,
                        help='Function: encrypt or decrypt')
    parser.add_argument('--file',
                        type=str,
                        required=True,
                        help='File path')
    parser.add_argument('--password',
                        type=str,
                        required=True,
                        help='Password to encrypt file')

    args = parser.parse_args()
    func = args.func
    password = args.password
    file_path = args.file

    print(f.renderText('encrypt file'))
    print('Encrypt or decrypt files with ONLY ONE COMMAND '
          '\n----------------------------------------------------------------------')
    print('PARAMETERS')
    print(f'func:\t\t{func}')
    print(f'password:\t{password}')
    print(f'file_path:\t{file_path}')
    print()

    readed_file = open_file(file_path)

    if 'encrypt' in func:
        encrypt_file(file_content=readed_file,
                     file_path=file_path,
                     passphrase=password)

    elif 'decrypt' in func:
        decrypt_file(file_content=readed_file,
                     file_path=file_path,
                     passphrase=password)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Execution time: {format_timespan(time.time() - start)}')
