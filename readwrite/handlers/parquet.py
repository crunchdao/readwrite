from .base import Handler, Param


class ParquetHandler(Handler):

    def __init__(self):
        super().__init__(
            "parquet",
            ["parquet"]
        )

    def read(self, path, **kwargs):
        import pandas

        return pandas.read_parquet(path, **kwargs)

    def read_params(self):
        return {
            "engine": str,
            "columns": Param(str, multiple=True)
        }

    def write(self, x, path, **kwargs):
        import pandas

        if not isinstance(x, pandas.DataFrame):
            raise ValueError("value must be a dataframe")

        x.to_parquet(path, **kwargs)

    def write_params(self):
        return {
            "engine": str,
            "index": bool,
        }
