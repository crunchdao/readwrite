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

| Handler | Extensions | Backend | Read | Write |
| --- | --- | --- |:---:|:---:|
| [Binary](./readwrite/handlers/binary.py) | `bin` | [Python's `bytes`](https://docs.python.org/3/library/stdtypes.html#bytes) | :heavy_check_mark: | :heavy_check_mark: |
| [Csv](./readwrite/handlers/csv.py) | `csv` | [`pandas`](https://pandas.pydata.org/) | :heavy_check_mark: | :heavy_check_mark: |
| [Excel](./readwrite/handlers/excel.py) | `xlsx` | [`pandas`](https://pandas.pydata.org/) | :heavy_check_mark: | :heavy_check_mark: |
| [Joblib](./readwrite/handlers/joblib.py) | `joblib` | [`joblib`](https://joblib.readthedocs.io/) | :heavy_check_mark: | :heavy_check_mark: |
| [Json](./readwrite/handlers/json.py) | `json` | [Python's `json`](https://docs.python.org/3/library/json.html) | :heavy_check_mark: | :heavy_check_mark: |
| [Parquet](./readwrite/handlers/parquet.py) | `parquet` | [`pandas`](https://pandas.pydata.org/) | :heavy_check_mark: | :heavy_check_mark: |
| [Pickle](./readwrite/handlers/pickle.py) | `pkl`, `pickle` | [Python's `pickle`](https://docs.python.org/3/library/pickle.html) or [`pandas`](https://pandas.pydata.org/) | :heavy_check_mark: | :heavy_check_mark: |
| [Toml](./readwrite/handlers/toml.py) | `toml` | [`toml`](https://pypi.org/project/toml/) | :heavy_check_mark: | :heavy_check_mark: |
| [Tar](./readwrite/handlers/tar.py) | `tar` | [Python's `tarfile`](https://docs.python.org/3/library/tarfile.html) | :heavy_check_mark: | :x: |
| [Text](./readwrite/handlers/text.py) | `txt` | [Python's `str`](https://docs.python.org/3/library/stdtypes.html#str) | :heavy_check_mark: | :heavy_check_mark: |
| [Yaml](./readwrite/handlers/yaml.py) | `yml`, `yaml` | [`PyYAML`](https://pyyaml.org/) | :heavy_check_mark: | :heavy_check_mark: |
| [Zarr](./readwrite/handlers/zarr.py) | `zarr` | [`SpatialData`](https://spatialdata.scverse.org/en/stable/) | :heavy_check_mark: | :x: |
| [Zip](./readwrite/handlers/zip.py) | `zip` | [Python's `zipfile`](https://docs.python.org/3/library/zipfile.html) | :heavy_check_mark: | :x: |
