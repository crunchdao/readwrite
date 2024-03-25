from .base import Handler, Param


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
            "index_col": Param(
                int,
                help="Column to use as row label, denoted by column index.",
            ),
            "delimiter": Param(
                str,
                help="Character or regex pattern to treat as the delimiter",
            ),
            "skiprows": Param(
                int,
                help="Number of lines to skip at the start of the file.",
            ),
            "nrows": Param(
                int,
                help="Number of rows of file to read.",
            ),
            "verbose": Param(
                bool,
                is_flag=True,
                help="Indicate number of NA values placed in non-numeric columns.",
            ),
            "skip_blank_lines": Param(
                bool,
                is_flag=True,
                help="If True, skip over blank lines rather than interpreting as NaN values.",
            )
        }

    def write(self, x, path, **kwargs):
        import pandas

        if not isinstance(x, pandas.DataFrame):
            raise ValueError("value must be a dataframe")

        x.to_csv(path, **kwargs)

    def write_params(self):
        return {
            "index": Param(
                bool,
                help="Write row names (index)."
            ),
        }
