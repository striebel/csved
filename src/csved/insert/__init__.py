import argparse
import textwrap


from .row import init_parser as init_parser_insert_row
from .col import init_parser as init_parser_insert_col


NAME = PROG = 'insert'
DESCRIPTION = \
    textwrap.dedent(
        '''\
        insert a row or a column into the csv file'''
    )

# prc  : parser root children
# prci : parser root children insert
# prcia: parser root children insert args

PRCIA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prc: argparse._SubParsersAction
) -> argparse.ArgumentParser:
    assert isinstance(prc, argparse._SubParsersAction), type(prc)
    prci = prc.add_parser(NAME, **PRCIA)
    assert isinstance(prci, argparse.ArgumentParser), type(prci)
    
    # prcic: parser root children insert children
    prcic = prci.add_subparsers(required=True)
    assert isinstance(prcic, argparse._SubParsersAction), type(prcic)
    
    # prcicr: parser root children insert children row
    prcicr = init_parser_insert_row(prcic=prcic)
    assert isinstance(prcicr, argparse.ArgumentParser), type(prcicr)
    assert 'row' == prcicr.prog, prcicr.prog
    del prcicr

    # prcicc: parser root children insert children col
    prcicc = init_parser_insert_col(prcic=prcic)
    assert isinstance(prcicc, argparse.ArgumentParser), type(prcicc)
    assert 'col' == prcicc.prog, prcicc.prog
    del prcicc
    
    del prcic

    return prci




