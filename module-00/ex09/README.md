# ft_package

A sample test package.

## Features
- Arithmetic: `add`, `sub`, `mul`, `div`
- Utility: `count_in_list`

## Installation
Build the package (from inside `ex09/`):
```bash
python -m pip install --upgrade build wheel
python -m build
```
Install one of the artifacts:
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage
```python
from ft_package import count_in_list, add, sub, mul, div

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0

print(add(2, 3))   # 5
print(sub(5, 2))   # 3
print(mul(3, 4))   # 12
print(div(10, 2))  # 5.0
```

## Metadata (as shown by pip)
- Name: ft_package
- Version: 0.0.1
- Summary: A sample test package
- License: MIT