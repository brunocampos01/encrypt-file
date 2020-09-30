import argparse
import os
import subprocess
from pyfiglet import Figlet

f = Figlet(font='slant')
HERE = os.path.abspath(os.path.dirname(__file__))


def main():
    parser = argparse.ArgumentParser()
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
    print('Encrypt or decrypt files with ONLY ONE COMAND '
          '\n----------------------------------------------------------------------')
    print('PARAMETERS')
    print(f'func:\t\t{func}')
    print(f'password:\t{password}')
    print(f'file_path:\t{file_path}')
    print()

    subprocess.call(f"python3 {HERE}/encryptfile.py --func {func} --file {file_path} --password {password}",
                   shell=True)


if __name__ == '__main__':
    main()
