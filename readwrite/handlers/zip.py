from .base import Handler

"""
A better child based system need to be introduced instead of just opening a ZipFile.

Something like a DirectoryLike object, able to list, read, write and delete with a unified API.
"""

class ZipHandler(Handler):

    def __init__(self):
        super().__init__(
            "zip",
            ["zip"]
        )

    def read(self, path, **kwargs):
        import zipfile

        return zipfile.ZipFile(path, 'r', **kwargs)
