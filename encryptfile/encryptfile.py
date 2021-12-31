#!/usr/bin/python3
import binascii
import hashlib
import os
import sys
from binascii import hexlify
from binascii import unhexlify

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# colors
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ENDC = '\033[0m'


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
    iv_random = os.urandom(12)
    plaintext = plaintext.encode("utf8")
    ciphertext = aes.encrypt(iv_random, plaintext, None)
    return "%s-%s-%s" % (hexlify(salt).decode("utf8"),
                         hexlify(iv_random).decode("utf8"),
                         hexlify(ciphertext).decode("utf8"))


def decrypt(passphrase: str, ciphertext: str) -> str:
    try:
        salt, iv_random, ciphertext = map(unhexlify, ciphertext.split("-"))
    except binascii.Error:
        return sys.exit(f'{WARNING}File is not encrypted!{ENDC}')
    except ValueError:
        return sys.exit(f'{WARNING}The file is empty!{ENDC}')

    key, _ = derive_key(passphrase, salt)
    aes = AESGCM(key)
    plaintext = aes.decrypt(iv_random, ciphertext, None)

    return plaintext.decode("utf8")


def open_file(file_path: str) -> str:
    with open(file_path, 'r') as reader:
        return str(reader.read())


def encrypt_file(file_content: str, file_path: str, passphrase: str) -> None:
    print(f'Encrypting ...')
    encrypted_file = encrypt(passphrase=passphrase, plaintext=file_content)
    with open(file_path + ".enc", 'w') as writer:
        writer.write(encrypted_file)

    print(f'{OKGREEN}Encrypted file at {file_path}.enc{ENDC}')


def decrypt_file(file_content: str, file_path: str, passphrase: str) -> None:
    print(f'Decrypting ...')
    decrypted_file = decrypt(passphrase=passphrase, ciphertext=file_content)
    with open(file_path, 'w') as writer:
        writer.write(decrypted_file)

    print(f'{OKGREEN}File {file_path} decrypted{ENDC}')
