import argparse

from .row  import init_parser as init_parser_ed_row
from .cell import init_parser as init_parser_ed_cell


NAME = PROG = 'ed'
DESCRIPTION = 'edit a row, a column, or a cell in the csv file'



def init_parser(prc):
    # prc: parser root children
    assert isinstance(prc, argparse._SubParsersAction), type(prc)
    # prce: parser root children ed
    prce = prc.add_parser(NAME, prog=PROG, description=DESCRIPTION)
    del prc
    assert isinstance(prce, argparse.ArgumentParser), type(prce)

    prcec = prce.add_subparsers(required=True)
    assert isinstance(prcec, argparse._SubParsersAction), type(prcec)

    prcecr = init_parser_ed_row(prcec=prcec)
    assert isinstance(prcecr, argparse.ArgumentParser), type(prcecr)
    assert 'row' == prcecr.prog, prcecr.prog
    del prcecr

    prcecc = init_parser_ed_cell(prcec=prcec)
    assert isinstance(prcecc, argparse.ArgumentParser), type(prcecc)
    assert 'cell' == prcecc.prog, prcecc.prog
    del prcecc

    del prcec

    return prce





