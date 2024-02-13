from .base import Handler


class ExcelHandler(Handler):

    def __init__(self):
        super().__init__(
            "excel",
            ["xlsx"]
        )

    def read(self, path: str, **kwargs):
        import pandas

        return pandas.read_excel(path, **kwargs)

    def read_params(self):
        return {
            "sheet_name": str,
            "engine": str,
        }

    def write(self, x, path, **kwargs):
        import pandas

        if not isinstance(x, pandas.DataFrame):
            raise ValueError("value must be a dataframe")

        x.to_excel(path, **kwargs)

    def write_params(self):
        return {
            "index": bool,
            "sheet_name": str,
        }
