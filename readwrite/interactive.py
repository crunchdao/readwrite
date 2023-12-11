import code
import importlib
import os
import rlcompleter
import sys
import typing

import tqdm

from .constants import LOGGER
from .handlers.base import Handler
from .registry import Registry


def guess_name(x: typing.Any):
    try:
        import pandas
        if isinstance(x, pandas.DataFrame):
            return "df"
    except NameError:
        pass

    return "x"


def load_common_imports():
    imports = {
        "sys": sys,
        "os": os,
        "tqdm": tqdm,
    }

    def load(name: str, aliases=[]):
        nonlocal imports

        try:
            module = importlib.import_module(name)
        except NameError as error:
            print(f"cannot load {name}: {error}", file=sys.stderr)

        imports[name] = module
        for alias in aliases:
            imports[alias] = module

    load("json")
    load("pandas", ["pd"])

    return imports


def _load_files(
    registry: Registry,
    file_paths: typing.List[str],
    handler: typing.Optional[Handler],
    kwargs
):
    def do_read(file_path: str):
        try:
            if handler is None:
                return registry.read(file_path, **kwargs)
            else:
                LOGGER.debug(
                    "read - handler=%s path=`%s`",
                    handler.name, file_path
                )

                return handler.read(file_path, **kwargs)
        except Exception as exception:
            tqdm.tqdm.write(
                f"cannot load `{file_path}`: {exception}", file=sys.stderr)

    return {
        file_path: do_read(file_path)
        for file_path in tqdm.tqdm(file_paths)
    }


def _get_readline():
    if os.name == 'nt':
        import pyreadline3
        return pyreadline3.Readline()
    else:
        import readline
        return readline


def start_session(
    registry: Registry,
    file_paths: typing.Iterable[str],
    handler: typing.Optional[Handler] = None,
    kwargs={},
    history_file_path: str = ""
):
    file_paths = list(file_paths)
    files = _load_files(registry, file_paths, handler, kwargs)

    if len(files) == 1:
        first = next(iter(files.values()))
        names = {
            guess_name(first): first
        }
    else:
        names = {
            f"{guess_name(value)}{index}": value
            for index, value in enumerate(files.values())
        }

    paths = {
        f"{name}_path": path
        for name, path in zip(names.keys(), files.keys())
    }

    imports = load_common_imports()

    def _read(path: str, **kwargs):
        return registry.read(path, **kwargs)

    def _write(x: typing.Any, path: str, **kwargs):
        registry.write(x, path, **kwargs)

    locals = {
        "read": _read,
        "write": _write,
        "files": files,
        **paths,
        **names,
        **imports,
    }

    banner = "available variables:\n"
    for (name, value), (path_name, path) in zip(names.items(), paths.items()):
        type_name = value.__class__.__name__
        banner += f"{name}: {type_name}\n"
        banner += f"{path_name}: {path}\n"

    readline = _get_readline()
    readline.set_completer(rlcompleter.Completer(locals).complete)
    readline.parse_and_bind("tab: complete")

    history_file_path = os.path.expanduser(history_file_path)
    if os.path.exists(history_file_path):
        readline.read_history_file(history_file_path)

    console = code.InteractiveConsole(locals)
    console.interact(
        banner=banner,
        exitmsg=""
    )

    readline.write_history_file(history_file_path)
