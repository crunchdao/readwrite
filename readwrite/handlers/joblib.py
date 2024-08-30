from .base import Handler


class JoblibHandler(Handler):

    def __init__(self):
        super().__init__(
            "joblib",
            ["joblib"]
        )

    def read(self, path: str, **kwargs):
        import joblib

        return joblib.load(path, **kwargs)

    def write(self, x, path, **kwargs):
        import joblib

        joblib.dump(x, path, **kwargs)
