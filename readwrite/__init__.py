import typing

from .registry import get_global_registry


def read(path: str, **kwargs):
    return get_global_registry().read(path, **kwargs)


def write(x: typing.Any, path: str, **kwargs):
    get_global_registry().write(x, path, **kwargs)
