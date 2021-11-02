# Hypermodern Python

https://cjolowicz.github.io/posts/hypermodern-python-01-setup/

## Run tests

Linters also run by default

```
nox -r
```

To run only the linters

```
nox -rs lint
```

## Format code

```
nox -rs black
```
