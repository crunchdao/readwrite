from .base import Handler


class TextHandler(Handler):

    def __init__(self):
        super().__init__(
            "text",
            ["txt"]
        )

    def read(self, path, **kwargs):
        with open(path, "r") as fd:
            return fd.read()

    def write(self, x, path, **kwargs):
        with open(path, "w") as fd:
            fd.write(x)
