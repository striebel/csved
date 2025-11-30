import argparse

from .ed_row import ed_row


NAME = PROG = 'row'
DESCRIPTION = 'edit a row in the csv file'


def init_parser(prcec):
    # prcec: parser root children ed children
    assert isinstance(prcec, argparse._SubParsersAction), type(prcec)
    prcecr = prcec.add_parser(NAME, prog=PROG, description=DESCRIPTION)
    del prcec
    assert isinstance(prcecr, argparse.ArgumentParser), type(prcecr)

    prcecr.add_argument(
        '-r',
        '--rowidx',
        dest     = 'rowidx',
        type     = int,
        required = True,
    )
    prcecr.add_argument(
        'csv_file_path',
    )
    prcecr.set_defaults(func=ed_row)

    return prcecr




