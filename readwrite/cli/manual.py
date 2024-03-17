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
        params = {}
        for key, value in kwargs.items():
            if isinstance(value, tuple):
                if len(value):
                    value = list(value)
                else:
                    value = None

            if value is not None:
                params[key] = value

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
            is_flag = value.is_flag
            help = value.help
        else:
            multiple = False
            type = value
            is_flag = value == bool
            help = None

        key = key.replace("_", "-")
        func = click.option(
            f"--{key}",
            type=type,
            multiple=multiple,
            is_flag=is_flag,
            default=None,
            help=help
        )(func)

    cli.command(name=handler.name)(func)
