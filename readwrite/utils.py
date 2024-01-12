import time
import contextlib

from .constants import LOGGER


@contextlib.contextmanager
def measure_duration(operation: str, handler_name: str, path: str):
    start_time = time.time()

    LOGGER.debug(
        "%s - handler=%s path=`%s`",
        operation, handler_name, path
    )

    try:
        yield
    finally:
        end_time = time.time()
        duration = end_time - start_time

        LOGGER.debug(
            "%s - handler=%s path=`%s` duration=%.4fs",
            operation, handler_name, path, duration
        )
