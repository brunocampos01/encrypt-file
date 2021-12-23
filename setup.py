import os

from setuptools import find_packages
from setuptools import setup
from pip._internal.req import parse_requirements


here = os.path.abspath(os.path.dirname(__file__))
requirements_path = os.path.join(here, 'requirements.txt')
install_reqs = parse_requirements(requirements_path, session=False)

try:
    requirements = [str(ir.req) for ir in install_reqs]
except AttributeError:
    requirements = [str(ir.requirement) for ir in install_reqs]

# The text of the README file
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

setup(name='encrypt-file',
      version='2.1',
      packages=find_packages(),
      install_requires=requirements,
            entry_points={
          'console_scripts': ['encrypt-file=encryptfile.__main__:main']
      },
      # metadata to display on PyPI
      description='CLI to encrypt or decrypt files with ONLY ONE COMAND',
      long_description=README,
      long_description_content_type='text/markdown',
      keywords='encrypt, decrypt, cli, easy, file',
      url='https://github.com/brunocampos01/encrypt-file',  # project home page
      author='Bruno Campos',
      author_email='brunocampos01@gmail.com',
      license='MIT',
      platforms='any',
      classifiers=[
          'Programming Language :: Python',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License'
      ]
      )
