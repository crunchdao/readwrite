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
            "engine": Param(
                str,
                help="Parquet library to use."
            ),
            "columns": Param(
                str,
                multiple=True,
                help="If not None, only these columns will be read from the file."
            )
        }

    def write(self, x, path, **kwargs):
        import pandas

        if not isinstance(x, pandas.DataFrame):
            raise ValueError("value must be a dataframe")

        x.to_parquet(path, **kwargs)

    def write_params(self):
        return {
            "engine": Param(
                str,
                help="Parquet library to use."
            ),
            "index": Param(
                bool,
                is_flag=True,
                help="Include the dataframe's index(es) in the file output."
            ),
        }
