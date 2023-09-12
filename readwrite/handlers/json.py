from .base import Handler


class JsonHandler(Handler):

    def __init__(self):
        super().__init__(
            "json",
            ["json"]
        )

    def read(self, path, **kwargs):
        import json

        with open(path, "r") as fd:
            return json.load(fd)

    def write(self, x, path, **kwargs):
        import json

        with open(path, "w") as fd:
            return json.dump(x, fd)
