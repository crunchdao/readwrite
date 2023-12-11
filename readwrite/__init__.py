import logging
import typing

from .constants import LOGGER
from .registry import get_global_registry


def read(path: str, **kwargs) -> typing.Any:
    if path is None:
        return None

    return get_global_registry().read(path, **kwargs)


def read_as(path: str, extension: str, **kwargs) -> typing.Any:
    if path is None:
        return None

    return get_global_registry().read_as(path, extension, **kwargs)


def write(x: typing.Any, path: str, **kwargs) -> typing.Any:
    if x is None or path is None:
        return None

    get_global_registry().write(x, path, **kwargs)
    return x


def write_as(x: typing.Any, path: str, extension: str, **kwargs) -> typing.Any:
    if x is None or path is None:
        return None

    get_global_registry().write_as(x, path, extension, **kwargs)
    return x


def debug(state: bool):
    if state:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.NOTSET)
