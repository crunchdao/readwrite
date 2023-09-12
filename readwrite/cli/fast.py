import click
import typing

from ..registry import get_global_registry
from ..interactive import start_session
from ..constants import DEFAULT_HISTORY_FILE_PATH


@click.command()
@click.option("--history-file", default=DEFAULT_HISTORY_FILE_PATH)
@click.argument("file-paths", nargs=-1, type=click.Path(exists=True))
def cli(
    history_file: str,
    file_paths: typing.Tuple[str]
):
    registry = get_global_registry()

    start_session(
        registry,
        file_paths,
        history_file_path=history_file
    )
