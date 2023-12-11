import typing

import click

from ..constants import DEFAULT_HISTORY_FILE_PATH
from ..interactive import start_session
from ..registry import get_global_registry
from .utils import enable_debug


@click.command()
@click.option("--debug", is_flag=True)
@click.option("--history-file", default=DEFAULT_HISTORY_FILE_PATH)
@click.argument("file-paths", nargs=-1, type=click.Path(exists=True))
def cli(
    debug: bool,
    history_file: str,
    file_paths: typing.Tuple[str]
):
    enable_debug(debug)

    registry = get_global_registry()

    start_session(
        registry,
        file_paths,
        history_file_path=history_file
    )
