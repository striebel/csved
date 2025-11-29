import argparse

from .cmp_row import cmp_row

NAME = PROG = 'row'
DESCRIPTION = 'compare two rows in the csv file to each other'


# prcpc: parser root children cmp children
def init_parser(prcpc):
    assert isinstance(prcpc, argparse._SubParsersAction), type(prcpc)

    prcpcr = prcpc.add_parser(NAME, prog=PROG, description=DESCRIPTION)
    del prcpc
    assert isinstance(prcpcr, argparse.ArgumentParser), type(prcpcr)

    prcpcr.add_argument(
        '-a',
        '--a-rowidx',
        dest     = 'a_rowidx',
        type     = int,
        required = True,
    )
    prcpcr.add_argument(
        '-b',
        '--b-rowidx',
        dest     = 'b_rowidx',
        type     = int,
        required = True,
    )
    prcpcr.add_argument(
        'csv_file_path',
    )
    prcpcr.set_defaults(func=cmp_row)

    return prcpcr




