import sys

import qhue

from .cli import cli
from . import cfg

def main():
    """Entry point
    
    Also used to trap Qhue exceptions, as these are (almost?) always
    due to user input errors, so we don't want an ugly traceback.
    """
    try:
        cli()
    except qhue.qhue.QhueException as e:
        if cfg.traceback:
            raise
        else:
            print(f'Error from Hue: {e}')
            sys.exit(1)
