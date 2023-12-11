import logging

from ..__init__ import debug as do_enable_debug


def enable_debug(state: bool):
    logging.basicConfig(level=logging.INFO)

    do_enable_debug(state)
