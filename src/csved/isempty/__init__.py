import argparse

from .row import init_parser as init_parser_isempty_row


NAME = PROG = 'isempty'
DESCRIPTION = 'check if a row or column in the csv file is empty'

# prcma: parser root children isempty args

PRCMA = {'prog': PROG, 'description': DESCRIPTION}


def init_parser(
    prc: argparse._SubParsersAction
) -> argparse.ArgumentParser:

    assert isinstance(prc, argparse._SubParsersAction), type(prc)
    prcm = prc.add_parser(NAME, **PRCMA)
    del prc
    assert isinstance(prcm, argparse.ArgumentParser), type(prcm)

    prcmc = prcm.add_subparsers(required=True)
    assert isinstance(prcmc, argparse._SubParsersAction), type(prcmc)

    prcmcr = init_parser_isempty_row(prcmc=prcmc)
    assert isinstance(prcmcr, argparse.ArgumentParser), type(prcmcr)
    assert 'row' == prcmcr.prog, prcmcr.prog
    del prcmcr

    return prcm


