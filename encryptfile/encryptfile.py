#!/usr/bin/python3
import argparse
import time
import os

import hashlib
from pyfiglet import Figlet
from binascii import hexlify
from binascii import unhexlify
from humanfriendly import format_timespan
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

f = Figlet(font='slant')
HERE = os.path.abspath(os.path.dirname(__file__))


def derive_key(passphrase: str, salt: bytes = None) -> [str, bytes]:
    if salt is None:
        salt = os.urandom(8)
    
    return hashlib.pbkdf2_hmac(hash_name="sha256",
                               password=passphrase.encode("utf8"),
                               salt=salt,
                               iterations=10000), salt


def encrypt(passphrase: str, plaintext: str) -> str:
    key, salt = derive_key(passphrase)
    aes = AESGCM(key)
    iv = os.urandom(12)
    plaintext = plaintext.encode("utf8")
    ciphertext = aes.encrypt(iv, plaintext, None)
    return "%s-%s-%s" % (hexlify(salt).decode("utf8"), hexlify(iv).decode("utf8"), hexlify(ciphertext).decode("utf8"))


def decrypt(passphrase: str, ciphertext: str) -> str:
    salt, iv, ciphertext = map(unhexlify, ciphertext.split("-"))
    key, _ = derive_key(passphrase, salt)
    aes = AESGCM(key)
    plaintext = aes.decrypt(iv, ciphertext, None)

    return plaintext.decode("utf8")


def open_file(file_path: str) -> str:
    with open(file_path, 'r') as reader:
        return str(reader.read())


def encrypt_file(file_content: str, file_path: str, passphrase: str) -> None:
    print(f'Encrypting ...')

    with open(file_path + ".enc", 'w') as writer:
        writer.write(encrypt(passphrase=passphrase, plaintext=file_content))

    print(f'Encrypted file at {file_path}.enc')


def decrypt_file(file_content: str, file_path: str, passphrase: str) -> None:
    print(f'Decrypting ...')

    with open(file_path, 'w') as fo:
        fo.write(decrypt(passphrase=passphrase, ciphertext=file_content))

    print(f'File {file_path} decrypted')


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


    if 'encrypt' in func:
        file = open_file(file_path)
        encrypt_file(file_content=file,
                     file_path=file_path,
                     passphrase=password)

    elif 'decrypt' in func:
        encrypted_file = open_file(file_path)
        decrypt_file(file_content=encrypted_file,
                     file_path=file_path,
                     passphrase=password)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Execution time: {format_timespan(time.time() - start)}')
