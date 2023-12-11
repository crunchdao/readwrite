import os
import typing

from .constants import LOGGER
from .handlers.base import Handler


class UnknownExtension(ValueError):
    def __init__(self, extension: str):
        super().__init__(f"unknown extension: {extension}")

        self.extension = extension


class Registry:
    handlers = typing.List[Handler]

    def __init__(self):
        self.handlers = []

    def add(self, handler: Handler):
        self.handlers.append(handler)

    def read(self, path: str, **kwargs):
        handler = self.get(path)

        LOGGER.debug(
            "read - handler=%s path=`%s`",
            handler.name, path
        )

        return handler.read(path, **kwargs)

    def read_as(self, path: str, extension: str, **kwargs):
        handler = self.get(extension)

        LOGGER.debug(
            "read - handler=%s path=`%s`",
            handler.name, path
        )

        return handler.read(path, **kwargs)

    def write(self, x: typing.Any, path: str, **kwargs):
        handler = self.get(path)

        LOGGER.debug(
            "write - handler=%s path=`%s`",
            handler.name, path
        )

        handler.write(x, path, **kwargs)

    def write_as(self, x: typing.Any, path: str, extension: str, **kwargs):
        handler = self.get(extension)

        LOGGER.debug(
            "write - handler=%s path=`%s`",
            handler.name, path
        )

        handler.write(x, path, **kwargs)

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

        raise UnknownExtension(extension)

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

        from .handlers.yaml import YamlHandler
        self.add(YamlHandler())


_REGISTRY: Registry = None


def get_global_registry():
    global _REGISTRY

    if _REGISTRY is None:
        _REGISTRY = Registry()
        _REGISTRY.add_defaults()

    return _REGISTRY
