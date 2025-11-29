import argparse

from .row import init_parser as init_parser_cmp_row

NAME = PROG = 'cmp'
DESCRIPTION = 'compare two rows or two columns in the csv file to each other'


def init_parser(prc):
    assert isinstance(prc, argparse._SubParsersAction), type(prc)

    prcp = prc.add_parser(NAME, prog=PROG, description=DESCRIPTION)
    del prc
    assert isinstance(prcp, argparse.ArgumentParser), type(prcp)

    prcpc = prcp.add_subparsers(required=True)
    assert isinstance(prcpc, argparse._SubParsersAction), type(prcpc)

    prcpcr = init_parser_cmp_row(prcpc=prcpc)
    assert isinstance(prcpcr, argparse.ArgumentParser), type(prcpcr)
    assert 'row' == prcpcr.prog, prcpcr.prog
    del prcpcr

    del prcpc

    return prcp


