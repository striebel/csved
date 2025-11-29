import argparse

from .cp_row import cp_row


NAME = PROG = 'row'
DESCRIPTION = 'copy a row in the csv file'

# prcccra: parser root children cp children row args
PRCCCRA = {'prog': PROG, 'description': DESCRIPTION}

def init_parser(
    prccc: argparse._SubParsersAction,
) -> argparse.ArgumentParser:

    assert isinstance(prccc, argparse._SubParsersAction), type(prccc)
    prcccr = prccc.add_parser(NAME, **PRCCCRA)
    del prccc
    assert isinstance(prcccr, argparse.ArgumentParser), type(prcccr)
    
    prcccr.add_argument(
        '-s',
        '--src-rowidx',
        dest     = 'src_rowidx',
        type     = int,
        required = True,
    )
    prcccr.add_argument(
        '-d',
        '--dst-rowidx',
        dest     = 'dst_rowidx',
        type     = int,
        required = True,
    )
    prcccr.add_argument(
        'csv_file_path',
    )
    prcccr.set_defaults(func=cp_row)

    return prcccr



