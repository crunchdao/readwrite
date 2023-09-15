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

    def write(self, x: typing.Any, path: str, **kwargs):
        self.get(path).write(x, path, **kwargs)

    def get(self, path: str) -> Handler:
        try:
            path.index(".")
            _, dot_extension = os.path.splitext(path)
            extension = dot_extension[1:]
        except:
            extension = path

        for handler in self.handlers:
            if extension in handler.extensions:
                return handler

        raise ValueError(f"unknown extension: {dot_extension}")

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
