# Create a new release

## Update information

All the information of the release have to be in the file `setup.py`
Things to update:
- version


## Build The distribution

### Source distribution

Run the command

```
python setup.py sdist
```

### Binary distribution

First, delete the folders `build` and `dist`.

Run the command

```
python setup.py bdist_wheel
```

## Distribute it

Everything is specified in the file `.pypirc` in the home directory (`C:/Users/Vval`) 
(Account on *Pypi* and *test.pypi*)

### Upload it on test

Run the command

```
twine upload -r pypitest -p <password> dist/*
```

### Upload it

Run the command

```
twine upload -r pypi -p <password> dist/*
```

## Load it

### From test

```
pip install -i https://test.pypi.org/simple/ epic-path==0.0.0
```

### From non test

```
pip install epic-path
```

