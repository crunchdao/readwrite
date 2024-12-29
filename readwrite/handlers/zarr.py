from .base import Handler

class ZarrHandler(Handler):

    def __init__(self):
        super().__init__(
            "zarr",
            ["zarr"]
        )

    def read(self, path, **kwargs):
        import spatialdata

        return spatialdata.read_zarr(path, **kwargs)
