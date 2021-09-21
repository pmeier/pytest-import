# `pytest-import`

This is a proof-of-concept for https://github.com/pytest-dev/pytest/issues/8964#issuecomment-924289234.

The idea is to import test packages on the requested test paths if `pytest` runs with 
`--import-mode=importlib`.

## Demo

```shell
$ python setup.py develop
$ pytest --import-mode=importlib tests/
```

Although `tests/test_foo.py` features an import from `tests/utils.py`, we can 
`pytest --import-mode=importlib tests/` without error.
