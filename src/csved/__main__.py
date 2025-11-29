import sys
import argparse


from .hello .__main__ import init_parser as init_parser_hello
from .ls    .__main__ import init_parser as init_parser_ls
from .insert          import init_parser as init_parser_insert
from .delete          import init_parser as init_parser_delete
from .cp              import init_parser as init_parser_cp
from .isempty         import init_parser as init_parser_isempty
from .cmp             import init_parser as init_parser_cmp


def main() -> int:

    # pr: parser root 
    pr = argparse.ArgumentParser()

    # prc: parser root children
    prc = pr.add_subparsers(required=True)
    assert isinstance(prc, argparse._SubParsersAction), type(prc)

    # prch: parser root children hello
    prch = init_parser_hello(prc=prc)
    assert isinstance(prch, argparse.ArgumentParser), type(prch)
    assert 'hello' == prch.prog, prch.prog
    del prch

    # prcl: parser root children ls
    prcl = init_parser_ls(prc=prc)
    assert isinstance(prcl, argparse.ArgumentParser), type(prcl)
    assert 'ls' == prcl.prog, prcl.prog
    del prcl

    # prci: parser root children insert
    prci = init_parser_insert(prc=prc)
    assert isinstance(prci, argparse.ArgumentParser), type(prci)
    assert 'insert' == prci.prog, prci.prog
    del prci

    # prcd: parser root children delete
    prcd = init_parser_delete(prc=prc)
    assert isinstance(prcd, argparse.ArgumentParser), type(prcd)
    assert 'delete' == prcd.prog, prcd.prog
    del prcd

    # prcc: parser root children cp
    prcc = init_parser_cp(prc=prc)
    assert isinstance(prcc, argparse.ArgumentParser), type(prcc)
    assert 'cp' == prcc.prog, prcc.prog
    del prcc

    # prcm: parser root children isempty
    prcm = init_parser_isempty(prc=prc)
    assert isinstance(prcm, argparse.ArgumentParser), type(prcm)
    assert 'isempty' == prcm.prog, prcm.prog
    del prcm

    # prcp: parser root children cmp
    prcp = init_parser_cmp(prc=prc)
    assert isinstance(prcp, argparse.ArgumentParser), type(prcp)
    assert 'cmp' == prcp.prog, prcp.prog
    del prcp

    args = pr.parse_args()
    del pr
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




