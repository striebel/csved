import argparse

from .row import init_parser as init_parser_cp_row

NAME = PROG = 'cp'
DESCRIPTION = 'copy a row or a column in the csv file'

# prcca: parser root children cp args 
PRCCA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prc: argparse._SubParsersAction
) -> argparse.ArgumentParser:

    assert isinstance(prc, argparse._SubParsersAction), type(prc)
    prcc = prc.add_parser(NAME, **PRCCA)
    del prc
    assert isinstance(prcc, argparse.ArgumentParser), type(prcc)

    # parser root children cp children 
    prccc = prcc.add_subparsers(required=True)
    assert isinstance(prccc, argparse._SubParsersAction), type(prccc)

    # prcccr: parser root children cp children row
    prcccr = init_parser_cp_row(prccc=prccc)
    assert isinstance(prcccr, argparse.ArgumentParser), type(prcccr)
    assert 'row' == prcccr.prog, prcccr.prog
    del prcccr

    del prccc

    return prcc



