from .base import Handler


class TxtHandler(Handler):

    def __init__(self):
        super().__init__(
            "txt",
            ["txt"]
        )

    def read(self, path, **kwargs):
        with open(path, "r") as fd:
            return fd.read()

    def write(self, x, path, **kwargs):
        with open(path, "w") as fd:
            fd.write(x)
