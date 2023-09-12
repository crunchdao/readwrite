from .base import Handler


class PickleHandler(Handler):

    def __init__(self):
        super().__init__(
            "pickle",
            ["pkl", "pickle"]
        )

    def read(self, path, **kwargs):
        import pickle

        with open(path, "rb") as fd:
            return pickle.load(fd)

    def write(self, x, path, **kwargs):
        import pickle

        with open(path, "wb") as fd:
            return pickle.dump(x, fd)
