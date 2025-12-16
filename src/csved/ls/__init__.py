import sys
import argparse
import textwrap


from .row  import init_parser as init_parser_ls_row
from .col  import init_parser as init_parser_ls_col
from .cell import init_parser as init_parser_ls_cell


NAME = PROG = 'ls'
DESCRIPTION = \
    textwrap.dedent(
        '''\
        list contents of a csv file'''
    ).replace('\n', ' ')

# pr   : parser root
# prc  : parser root children
# prcl : parser root children ls
# prcla: parser root children ls args

PRCLA = {'prog': PROG, 'description': DESCRIPTION}



def init_parser(prc):
    assert isinstance(prc, argparse._SubParsersAction), type(prc)
    prcl = prc.add_parser(NAME, **PRCLA)
    del prc
    assert isinstance(prcl, argparse.ArgumentParser), type(prcl)

    # prclc: parser root children ls children
    prclc = prcl.add_subparsers(required=True)
    assert isinstance(prclc, argparse._SubParsersAction), type(prclc)

    # prclcr: parser root children ls children row
    prclcr = init_parser_ls_row(prclc=prclc)
    assert isinstance(prclcr, argparse.ArgumentParser), type(prclcr)
    assert 'row' == prclcr.prog, prclcr.prog
    del prclcr

    # prclcc: parser root children ls children col
    prclcc = init_parser_ls_col(prclc=prclc)
    assert isinstance(prclcc, argparse.ArgumentParser), type(prclcc)
    assert 'col' == prclcc.prog, prclcc.prog
    del prclcc

    # prclce: parser root children ls children cell
    prclce = init_parser_ls_cell(prclc=prclc)
    assert isinstance(prclce, argparse.ArgumentParser), type(prclce)
    assert 'cell' == prclce.prog, prclce.prog
    del prclce

    del prclc
    return prcl




