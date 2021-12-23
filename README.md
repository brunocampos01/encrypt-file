# :page_with_curl:	_encrypt file_ :lock: 
[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/downloads/release/python-381/)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)

Encrypt or decrypt files with ONLY ONE COMAND
```bash
                                    __     _____ __   
  ___  ____  ____________  ______  / /_   / __(_) /__ 
 / _ \/ __ \/ ___/ ___/ / / / __ \/ __/  / /_/ / / _ \
/  __/ / / / /__/ /  / /_/ / /_/ / /_   / __/ / /  __/
\___/_/ /_/\___/_/   \__, / .___/\__/  /_/ /_/_/\___/ 
                    /____/_/                          

Encrypt or decrypt files with ONLY ONE COMAND 
----------------------------------------------------------------------
PARAMETERS
func:		encrypt
password:	123456
file_path:	tests/plain_text.txt

Encrypting ...
Encrypted file at tests/plain_text.txt.enc
Execution time: 0.01 seconds                        
```
The _encrypt file_ is a **CLI** for encrypting and decrypting files.

## Why should I use the _encrypt file_?
- **No Code**: When there is no need to code something you can simply use _encrypt file_.
- **Abstraction of cryptographic algorithms**: you don't need to know what goes on behind the scenes in _encrypt file_ (but if you want, just see it on github).

## Requirements
This project is tested with:

| Requisite      | Version  |
|----------------|----------|
| Python         | 3.8.10   |
| Pip            | 21.2.4   |

## Install
```sh
pip install encrypt-file
```

## Usage
- :lock: Encrypt :lock:
```bash
encrypt-file \
          --func encrypt \
          --file plain_text.txt \
          --password 123456
```

- :unlock: Decrypt :unlock:
```bash
encrypt-file \
          --func decrypt \
          --file plain_text.txt.enc \
          --password 123456
```

## What is the security level?
- Even using low-quality passwords, _encrypt file_ tries to make things as secure as possible because it is implemented using **PBKDF2** key deviation with SHA256 hash, a 16-bit random salt and 10,000 rounds.

---

<p  align="left">
<br/>
<a href="mailto:brunocampos01@gmail.com" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/email.png" alt="Gmail" width="30">
</a>
<a href="https://stackoverflow.com/users/8329698/bruno-campos" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/stackoverflow.png" alt="GitHub" width="30">
</a>
<a href="https://www.linkedin.com/in/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/linkedin.png" alt="LinkedIn" width="30"></a>
<a href="https://github.com/brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/github.png" alt="GitHub" width="30"></a>
<a href="https://medium.com/@brunocampos01" target="_blank"><img src="https://github.com/brunocampos01/devops/blob/master/images/medium.png" alt="GitHub" width="30">
</a>
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png",  align="right" /></a><br/>
</p>
