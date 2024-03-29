from .base import Handler


class YamlHandler(Handler):

    def __init__(self):
        super().__init__(
            "yaml",
            ["yml", "yaml"]
        )

    def read(self, path, **kwargs):
        import yaml

        with open(path, "r") as fd:
            return yaml.full_load(fd, **kwargs)

    def write(self, x, path, **kwargs):
        import yaml

        with open(path, "w") as fd:
            yaml.dump(x, fd, **kwargs)
