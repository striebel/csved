import argparse


from .insert_col import insert_col


NAME = PROG = 'col'
DESCRIPTION = 'insert a column into the csv file'

# prcic  : parser root children insert children
# prcicc : parser root children insert children col
# prcicca: parser root children insert children col args

PRCICCA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prcic: argparse._SubParsersAction
) -> argparse.ArgumentParser:

    assert isinstance(prcic, argparse._SubParsersAction), type(prcic)
    prcicc = prcic.add_parser(NAME, **PRCICCA)
    del prcic
    assert isinstance(prcicc, argparse.ArgumentParser), type(prcicc)

    prcicc.add_argument(
        '-c',
        '--colidx',
        dest     = 'colidx',
        type     = int,
        required = True,
    )
    prcicc.add_argument(
        '-n',
        '--colname',
        dest     = 'colname',
        type     = str,
        required = False,
        default  = '',
    )
    prcicc.add_argument(
        'csv_file_path',
    )
    prcicc.set_defaults(func=insert_col)

    return prcicc


    
