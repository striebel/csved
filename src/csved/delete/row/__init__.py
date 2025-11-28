import argparse


from .delete_row import delete_row


NAME = PROG = 'row'
DESCRIPTION = 'delete a row in the csv file'

# prcdcr : parser root children delete children row
# prcdcra: parser root children delete children row args

PRCDCRA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prcdc: argparse._SubParsersAction
) -> argparse.ArgumentParser:

    assert isinstance(prcdc, argparse._SubParsersAction), type(prcdc)
    prcdcr = prcdc.add_parser(NAME, **PRCDCRA)
    del prcdc
    assert isinstance(prcdcr, argparse.ArgumentParser), type(prcdcr)
    assert PROG == prcdcr.prog, (PROG, prcdcr.prog)

    prcdcr.add_argument(
        '-r',
        '--rowidx',
        dest     = 'rowidx',
        type     = int,
        required = True,
    )
    prcdcr.add_argument(
        'csv_file_path'
    )
    prcdcr.set_defaults(func=delete_row)

    return prcdcr




