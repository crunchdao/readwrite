from .base import Handler, Param


class PickleHandler(Handler):

    def __init__(self):
        super().__init__(
            "pickle",
            ["pkl", "pickle"]
        )

    def read(self, path, **kwargs):
        use_pandas = kwargs.pop("pandas", False)

        if use_pandas:
            import pandas
            return pandas.read_pickle(path, **kwargs)

        import pickle
        with open(path, "rb") as fd:
            return pickle.load(fd, **kwargs)

    def read_params(self):
        return {
            "pandas": Param(
                bool,
                is_flag=True,
                help="Use `pandas.read_pickle()` instead of python's `pickle.load()`."
            ),
        }

    def write(self, x, path, **kwargs):
        use_pandas = kwargs.pop("pandas", False)

        if use_pandas:
            import pandas
            return pandas.to_pickle(x, path, **kwargs)

        import pickle
        with open(path, "wb") as fd:
            return pickle.dump(x, fd, **kwargs)

    def write_params(self):
        return {
            "pandas": Param(
                bool,
                is_flag=True,
                help="Use `pandas.to_pickle()` instead of python's `pickle.dump()`."
            ),
        }
