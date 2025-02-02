from .base import Handler


class H5adHandler(Handler):

    def __init__(self):
        super().__init__(
            "h5ad",
            ["h5ad"]
        )

    def read(self, path, **kwargs):
        import scanpy

        return scanpy.read_h5ad(path, **kwargs)
