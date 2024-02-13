import os
import typing

from .constants import LOGGER
from .handlers.base import Handler
from .utils import measure_duration

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

        with measure_duration("read", handler.name, path):
            return handler.read(path, **kwargs)

    def read_as(self, path: str, extension: str, **kwargs):
        handler = self.get(extension)

        with measure_duration("read_as", handler.name, path):
            return handler.read(path, **kwargs)

    def write(self, x: typing.Any, path: str, **kwargs):
        handler = self.get(path)

        with measure_duration("write", handler.name, path):
            handler.write(x, path, **kwargs)

    def write_as(self, x: typing.Any, path: str, extension: str, **kwargs):
        handler = self.get(extension)

        with measure_duration("write_as", handler.name, path):
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
        from .handlers.binary import BinaryHandler
        self.add(BinaryHandler())

        from .handlers.csv import CsvHandler
        self.add(CsvHandler())

        from .handlers.excel import ExcelHandler
        self.add(ExcelHandler())

        from .handlers.json import JsonHandler
        self.add(JsonHandler())

        from .handlers.parquet import ParquetHandler
        self.add(ParquetHandler())

        from .handlers.pickle import PickleHandler
        self.add(PickleHandler())

        from .handlers.toml import TomlHandler
        self.add(TomlHandler())

        from .handlers.text import TextHandler
        self.add(TextHandler())

        from .handlers.yaml import YamlHandler
        self.add(YamlHandler())


_REGISTRY: Registry = None


def get_global_registry():
    global _REGISTRY

    if _REGISTRY is None:
        registry = Registry()
        registry.add_defaults()

        _REGISTRY = registry

    return _REGISTRY
