import sys
import argparse
import textwrap


from .hello import print_hello


NAME = PROG = 'hello'
DESCRIPTION = \
    textwrap.dedent(
        '''\
        print a 'hello, world' message to stdout'''
    ).replace('\n', ' ')


# pr   : parser root
# prc  : parser root children
# prch : parser root children hello
# prcha: parser root children hello args

PRCHA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(prc):
    assert isinstance(prc, argparse._SubParsersAction), type(prc)
    prch = prc.add_parser(NAME, **PRCHA)
    del prc
    assert isinstance(prch, argparse.ArgumentParser), type(prch)

    prch.set_defaults(func=print_hello)

    return prch






