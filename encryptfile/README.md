# Notes About Create and Test This Project

## Publishing Module to PyPi
To upload package to PyPI, I used a tool called [Twine](https://twine.readthedocs.io/en/stable/).

### Building Package
To create a source archives (`build`, `dist`, `encrypt_file.egg-info`):
```
python setup.py sdist bdist_wheel
```

To create a source archives (`build`, `dist`, `encrypt_file.egg-info`):
```
twine check dist/*
```

### Upload
```
twine upload dist/*
```

---

## Execute Tests
```bash
pytest tests -vv
```
