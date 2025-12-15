import argparse

from .ls_cell import ls_cell

NAME = PROG = 'cell'
DESCRIPTION = 'show the contents of a cell in the csv file'

def init_parser(prclc):
    # prclc: parser root children ls children
    assert isinstance(prclc, argparse._SubParsersAction), type(prclc)
    # prclce: parser root children ls children cell
    prclce = prclc.add_parser(NAME, prog=PROG, description=DESCRIPTION)
    del prclc
    assert isinstance(prclce, argparse.ArgumentParser), type(prclce)
    
    prclce.add_argument(
        '-r',
        '--rowidx',
        dest     = 'rowidx',
        type     = int,
        required = True,
    )
    prclce.add_argument(
        '-c',
        '--colidx',
        dest     = 'colidx',
        type     = int,
        required = True,
    )
    prclce.add_argument(
        'csv_file_path',
    )
    prclce.set_defaults(
        func = ls_cell
    )

    return prclce




