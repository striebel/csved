import sys
import argparse
import textwrap


from .ls_col import ls_col


NAME = PROG = 'col'
DESCRIPTION = \
    textwrap.dedent(
        '''\
        list column(s) in a csv file'''
    )

# pr     : parser root 
# prc    : parser root children
# prcl   : parser root children ls
# prclc  : parser root children ls children
# prclcc : parser root children ls children col
# prclcca: parser root children ls children col args

PRCLCCA = {'prog': PROG, 'description': DESCRIPTION}



def init_parser(prclc):
    assert isinstance(prclc, argparse._SubParsersAction), type(prclc)
    prclcc = prclc.add_parser(NAME, **PRCLCCA)
    del prclc
    assert isinstance(prclcc, argparse.ArgumentParser), type(prclcc)

    prclcc.add_argument(
        'csv_file_path',
        type = str,
    )
    prclcc.set_defaults(func=ls_col)

    return prclcc







