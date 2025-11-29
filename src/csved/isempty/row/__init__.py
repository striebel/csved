import argparse

from .isempty_row import isempty_row

NAME = PROG = 'row'
DESCRIPTION = 'check if a row in the csv file is empty'

# prcmcra: parser root children isempty children row args
PRCMCRA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prcmc: argparse._SubParsersAction,
) -> argparse.ArgumentParser:

    assert isinstance(prcmc, argparse._SubParsersAction), type(prcmc)
    prcmcr = prcmc.add_parser(NAME, **PRCMCRA)
    del prcmc
    assert isinstance(prcmcr, argparse.ArgumentParser), type(prcmcr)
    
    prcmcr.add_argument(
        '-r',
        '--rowidx',
        dest     = 'rowidx',
        type     = int,
        required = True,
    )
    prcmcr.add_argument(
        'csv_file_path',
    )
    prcmcr.set_defaults(func=isempty_row)

    return prcmcr
