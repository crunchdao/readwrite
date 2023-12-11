import typing

import click

from ..constants import DEFAULT_HISTORY_FILE_PATH
from ..handlers.base import Param
from ..interactive import start_session
from ..registry import get_global_registry
from .utils import enable_debug

history_file: str


@click.group()
@click.option("--debug", is_flag=True)
@click.option("--history-file", "history_file_value", default=DEFAULT_HISTORY_FILE_PATH)
def cli(
    debug: bool,
    history_file_value: str
):
    enable_debug(debug)

    global history_file
    history_file = history_file_value


registry = get_global_registry()
for handler in registry.handlers:
    @click.argument("file-paths", nargs=-1, type=click.Path(exists=True))
    def func(
        file_paths: typing.Tuple[str],
        __handler=handler,
        **kwargs
    ):
        params = {
            key: None if isinstance(value, tuple) and not len(value) else value
            for key, value in kwargs.items()
        }

        params = {
            key: value
            for key, value in params.items()
            if value is not None
        }

        start_session(
            registry,
            file_paths,
            __handler,
            params,
            history_file
        )

    for key, value in handler.read_params().items():
        if isinstance(value, Param):
            multiple = value.multiple
            type = value.type
        else:
            multiple = False
            type = value

        func = click.option(
            f"--{key}",
            type=type,
            multiple=multiple,
            default=None
        )(func)

    cli.command(name=handler.name)(func)
