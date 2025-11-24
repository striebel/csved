import sys
import argparse
import textwrap


from .row.__main__ import init_parser as init_parser_ls_row
from .col.__main__ import init_parser as init_parser_ls_col


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



def init_parser(
    prc : argparse._SubParsersAction = None
) -> argparse.ArgumentParser:
    if prc is None:
        prcl = argparse.ArgumentParser(**PRCLA)
    else:
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

    del prclc
    return prcl



def main() -> int:
    # pr: parser root
    pr = init_parser()
    assert isinstance(pr, argparse.ArgumentParser), type(pr)
    assert PROG == pr.prog, (PROG, pr.prog)
    
    args = pr.parse_args()
    assert isinstance(args, argparse.Namespace), type(args)
    args = vars(args)
    assert isinstance(args, dict), type(args)
    func = args.pop('func')
    assert callable(func), func
    
    # es: exit status
    es = func(**args)
    del args, func
    assert isinstance(es, int), type(es)
    assert 0 <= es and es <= 255, es

    return es



if '__main__' == __name__:
    sys.exit(main())





