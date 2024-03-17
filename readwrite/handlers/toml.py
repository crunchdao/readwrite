from .base import Handler


class TomlHandler(Handler):

    def __init__(self):
        super().__init__(
            "toml",
            ["toml"]
        )

    def read(self, path, **kwargs):
        import toml

        with open(path, "r") as fd:
            return toml.load(fd, **kwargs)

    def write(self, x, path, **kwargs):
        import toml

        with open(path, "w") as fd:
            return toml.dump(x, fd, **kwargs)
