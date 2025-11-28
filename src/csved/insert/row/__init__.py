import argparse
import textwrap


from .insert_row import insert_row


NAME = PROG = 'row'
DESCRIPTION = \
    textwrap.dedent(
        '''\
        insert a row into the csv file'''
    )

# prcic  : parser root children insert children
# prcicr : parser root children insert children row
# prcicra: parser root children insert children row args

PRCICRA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prcic: argparse._SubParsersAction
) -> argparse.ArgumentParser:
    assert isinstance(prcic, argparse._SubParsersAction), type(prcic)
    prcicr = prcic.add_parser(NAME, **PRCICRA)
    del prcic
    assert isinstance(prcicr, argparse.ArgumentParser), type(prcicr)
    
    prcicr.add_argument(
        '-r',
        '--row-idx',
        dest     = 'row_idx',
        type     = int,
        default  = None,
        required = True,
    )
    prcicr.add_argument(
        'csv_file_path',
        type = str,
    )
    prcicr.set_defaults(func=insert_row)

    return prcicr




