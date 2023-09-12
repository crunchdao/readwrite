from .base import Handler


class CsvHandler(Handler):

    def __init__(self):
        super().__init__(
            "csv",
            ["csv"]
        )

    def read(self, path: str, **kwargs):
        import pandas

        return pandas.read_csv(path, **kwargs)

    def read_params(self):
        return {
            "index_col": int
        }

    def write(self, x, path, **kwargs):
        import pandas

        if not isinstance(x, pandas.DataFrame):
            raise ValueError("value must be a dataframe")

        x.to_csv(path, **kwargs)

    def write_params(self):
        return {
            "index": bool,
        }
