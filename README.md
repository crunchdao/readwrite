Quickly read and write file based on their extension.

[![PyTest](https://github.com/crunchdao/readwrite/actions/workflows/pytest.yml/badge.svg)](https://github.com/crunchdao/readwrite/actions/workflows/pytest.yml)

- [Install](#install)
- [CLI Usage](#cli-usage)
- [Code Usage](#code-usage)

## Install

```
python3 -m pip install --upgrade readwrite
```

## CLI Usage

```bash
readf [FILE-PATHS...]
```

or

```bash
readfile <EXTENSION> [EXTENSION-SPECIFIC-OPTIONS] [FILE-PATHS...]
```

## Code Usage

```python
import readwrite as rw

# will use pandas.read_csv(...)
df = rw.read("data.csv")

# will use pandas.to_parquet(...)
rw.write(df, "data.parquet")
```
