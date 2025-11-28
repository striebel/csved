import argparse


from .delete_col import delete_col


NAME = PROG = 'col'
DESCRIPTION = 'delete a column from the csv file'

# prcdc  : parser root children delete children
# prcdcc : parser root children delete children col
# prcdcca: parser root children delete children col args

PRCDCCA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prcdc: argparse._SubParsersAction
) -> argparse.ArgumentParser:

    assert isinstance(prcdc, argparse._SubParsersAction), type(prcdc)
    prcdcc = prcdc.add_parser(NAME, **PRCDCCA)
    del prcdc
    assert isinstance(prcdcc, argparse.ArgumentParser), type(prcdcc)

    prcdcc.add_argument(
        '-c',
        '--colidx',
        dest     = 'colidx',
        type     = int,
        required = True,
    )
    prcdcc.add_argument(
        'csv_file_path',
    )
    prcdcc.set_defaults(func=delete_col)

    return prcdcc


    
