from .base import Handler


class TarHandler(Handler):

    def __init__(self):
        super().__init__(
            "tar",
            ["tar"]
        )

    def read(self, path, **kwargs):
        import tarfile

        return tarfile.TarFile(path, 'r', **kwargs)
