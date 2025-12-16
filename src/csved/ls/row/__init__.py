import sys
import argparse 
import textwrap


from .ls_row import ls_row


NAME = PROG = 'row'
DESCRIPTION = \
    textwrap.dedent(
        '''\
        list row(s) in a csv file'''
    ).replace('\n', ' ')

# pr     : parser root
# prc    : parser root children
# prcl   : parser root children ls
# prclc  : parser root children ls children
# prclcr : parser root children ls children row
# prclcra: parser root children ls children row args

PRCLCRA = {'prog': PROG, 'description': DESCRIPTION}



def init_parser(prclc):
    assert isinstance(prclc, argparse._SubParsersAction), type(prclc)
    prclcr = prclc.add_parser(NAME, **PRCLCRA)
    del prclc
    assert isinstance(prclcr, argparse.ArgumentParser), type(prclcr)
    
    prclcr.add_argument(
        '-r',
        '--rowidx',
        dest    = 'rowidx',
        metavar = 'rowidx',
        type    = int,
        default = None,
    )
    prclcr.add_argument(
        'csv_file_path',
        type = str,
    )
    prclcr.set_defaults(
        func = ls_row,
    )
    
    return prclcr







