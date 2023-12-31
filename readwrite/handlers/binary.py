from .base import Handler


class BinaryHandler(Handler):

    def __init__(self):
        super().__init__(
            "binary",
            ["bin"]
        )

    def read(self, path, **kwargs):
        with open(path, "rb") as fd:
            return fd.read()

    def write(self, x, path, **kwargs):
        with open(path, "wb") as fd:
            fd.write(x)
