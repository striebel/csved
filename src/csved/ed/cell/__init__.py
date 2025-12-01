import argparse

from .ed_cell import ed_cell


NAME = PROG = 'cell'
DESCRIPTION = 'edit a cell in the csv file'


def init_parser(prcec):
    
    assert isinstance(prcec, argparse._SubParsersAction), type(prcec)
    prcecc = prcec.add_parser(NAME, prog=PROG, description=DESCRIPTION)
    del prcec
    assert isinstance(prcecc, argparse.ArgumentParser), type(prcecc)
    
    prcecc.add_argument(
        '-r',
        '--rowidx',
        required = True,
        dest     = 'rowidx',
        type     = int,
    )
    prcecc.add_argument(
        '-c',
        '--colidx',
        required = True,
        dest     = 'colidx',
        type     = int,
    )
    prcecc.add_argument(
        '-v',
        '--cellvalue',
        required = True,
        dest     = 'cellvalue',
        type     = str,
    )
    prcecc.add_argument(
        'csv_file_path',
    )
    prcecc.set_defaults(func=ed_cell)

    return prcecc




