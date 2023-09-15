import typing

from .registry import get_global_registry


def read(path: str, **kwargs) -> typing.Any:
    if path is None:
        return None
    
    return get_global_registry().read(path, **kwargs)


def write(x: typing.Any, path: str, **kwargs) -> typing.Any:
    if x is None or path is None:
        return None
    
    get_global_registry().write(x, path, **kwargs)
    return x
