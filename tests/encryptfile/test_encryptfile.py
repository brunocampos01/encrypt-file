import os

import pytest
from encryptfile.encryptfile import decrypt_file
from encryptfile.encryptfile import encrypt_file
from encryptfile.encryptfile import open_file

here = os.path.abspath(os.path.dirname(__file__))


def test_decrypt_empty_file_not_encrypted():
    """
    The file is not encrypted.
    Test the decrypt empty_file. Return a raise SystemExit
    """
    file_path = f'{here}/../files/empty_file'
    password = '123456'
    file_content = open_file(file_path)

    # with pytest.raises(ValueError, match=r".*The file is empty.*"):
    with pytest.raises(SystemExit):
        decrypt_file(file_content=file_content,
                     file_path=file_path,
                     passphrase=password)


def test_decrypt_plain_text_not_encrypted():
    """
    The file is not encrypted.
    Test the decrypt plain_text. Return a raise SystemExit
    """
    file_path = f'{here}/../files/plain_text.txt'
    password = '123456'
    file_content = open_file(file_path)

    with pytest.raises(SystemExit):
        decrypt_file(file_content=file_content,
                     file_path=file_path,
                     passphrase=password)


def test_decrypt_xml_not_encrypted():
    """
    The file is not encrypted.
    Test the decrypt semi_structure_data. Return a raise SystemExit
    """
    file_path = f'{here}/../files/semi_structure_data.xml'
    password = '123456'
    file_content = open_file(file_path)

    with pytest.raises(SystemExit):
        decrypt_file(file_content=file_content,
                     file_path=file_path,
                     passphrase=password)


def test_encrypt_plain_text():
    """
    The file is not encrypted.
    Test the encrypt plain_text.txt. This function return a new file with pattern <ORIGINAL_NAME>.enc
    """
    file_path = f'{here}/../files/plain_text.txt'
    password = '123456'
    file_content = open_file(file_path)

    encrypt_file(file_content=file_content,
                 file_path=file_path,
                 passphrase=password)
    enc_file = open_file(f'{file_path}.enc')

    assert len(enc_file) > 0
