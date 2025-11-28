import argparse
import textwrap


from .row import init_parser as init_parser_delete_row
from .col import init_parser as init_parser_delete_col


NAME = PROG = 'delete'
DESCRIPTION = \
    textwrap.dedent(
        '''\
        delete a row or a column in the csv file'''
    )

# prc  : parser root children
# prcd : parser root children delete
# prcda: parser root children delete args

PRCDA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prc: argparse._SubParsersAction
) -> argparse.ArgumentParser:

    assert isinstance(prc, argparse._SubParsersAction), type(prc)
    prcd = prc.add_parser(NAME, **PRCDA)
    del prc
    assert isinstance(prcd, argparse.ArgumentParser), type(prcd)
    assert PROG == prcd.prog, (PROG, prcd.prog)
    
    prcdc = prcd.add_subparsers(required=True)
    assert isinstance(prcdc, argparse._SubParsersAction), type(prcdc)

    prcdcr = init_parser_delete_row(prcdc=prcdc)
    assert isinstance(prcdcr, argparse.ArgumentParser), type(prcdcr)
    assert 'row' == prcdcr.prog, prcdcr.prog
    del prcdcr

    prcdcc = init_parser_delete_col(prcdc=prcdc)
    assert isinstance(prcdcc, argparse.ArgumentParser), type(prcdcc)
    assert 'col' == prcdcc.prog, prcdcc.prog
    del prcdcc

    del prcdc    

    return prcd




