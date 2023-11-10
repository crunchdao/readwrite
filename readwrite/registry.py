import typing
import os

from .handlers.base import Handler


class Registry:

    handlers = typing.List[Handler]

    def __init__(self):
        self.handlers = []

    def add(self, handler: Handler):
        self.handlers.append(handler)

    def read(self, path: str, **kwargs):
        return self.get(path).read(path, **kwargs)

    def read_as(self, path: str, extension: str, **kwargs):
        return self.get(extension).read(path, **kwargs)

    def write(self, x: typing.Any, path: str, **kwargs):
        self.get(path).write(x, path, **kwargs)

    def write_as(self, x: typing.Any, path: str, extension: str, **kwargs):
        self.get(extension).write(x, path, **kwargs)

    def get(self, path_or_extension: str):
        try:
            path_or_extension.index(".")
            _, dot_extension = os.path.splitext(path_or_extension)
            extension = dot_extension[1:]
        except:
            extension = path_or_extension
        
        for handler in self.handlers:
            if extension in handler.extensions:
                return handler

        raise ValueError(f"unknown extension: {extension}")

    def add_defaults(self):
        from .handlers.csv import CsvHandler
        self.add(CsvHandler())

        from .handlers.json import JsonHandler
        self.add(JsonHandler())

        from .handlers.parquet import ParquetHandler
        self.add(ParquetHandler())

        from .handlers.pickle_ import PickleHandler
        self.add(PickleHandler())

        from .handlers.txt import TxtHandler
        self.add(TxtHandler())


_REGISTRY: Registry = None


def get_global_registry():
    global _REGISTRY

    if _REGISTRY is None:
        _REGISTRY = Registry()
        _REGISTRY.add_defaults()

    return _REGISTRY
