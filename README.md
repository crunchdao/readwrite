Quickly read and write file based on their extension.

[![PyTest](https://github.com/crunchdao/readwrite/actions/workflows/pytest.yml/badge.svg)](https://github.com/crunchdao/readwrite/actions/workflows/pytest.yml)

- [Install](#install)
- [CLI Usage](#cli-usage)
- [Code Usage](#code-usage)
- [Supported Extensions](#supported-extensions)

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

## Supported Extensions

| Handler | Extensions | Backend | Operations |
| --- | --- | --- | --- |
| [Binary](./readwrite/handlers/binary.py) | `bin` | [Python's `bytes`](https://docs.python.org/3/library/stdtypes.html#bytes) | `read` + `write` |
| [Csv](./readwrite/handlers/csv.py) | `csv` | [`pandas`](https://pandas.pydata.org/) | `read` + `write` |
| [Excel](./readwrite/handlers/excel.py) | `xlsx` | [`pandas`](https://pandas.pydata.org/) | `read` + `write` |
| [Json](./readwrite/handlers/json.py) | `json` | [Python's `json`](https://docs.python.org/3/library/json.html) | `read` + `write` |
| [Parquet](./readwrite/handlers/parquet.py) | `parquet` | [`pandas`](https://pandas.pydata.org/) | `read` + `write` |
| [Pickle](./readwrite/handlers/pickle.py) | `pkl`, `pickle` | [Python's `pickle`](https://docs.python.org/3/library/pickle.html) or [`pandas`](https://pandas.pydata.org/) | `read` + `write` |
| [Toml](./readwrite/handlers/toml.py) | `toml` | [`toml`](https://pypi.org/project/toml/) | `read` + `write` |
| [Text](./readwrite/handlers/text.py) | `txt` | [Python's `str`](https://docs.python.org/3/library/stdtypes.html#str) | `read` + `write` |
| [Yaml](./readwrite/handlers/yaml.py) | `yml`, `yaml` | [`PyYAML`](https://pyyaml.org/) | `read` + `write` |
| [Zip](./readwrite/handlers/zip.py) | `zip` | [Python's `zipfile`](https://docs.python.org/3/library/zipfile.html) | `read` |
