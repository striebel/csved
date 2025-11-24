import sys
import argparse


from .hello.__main__ import init_parser as init_parser_hello 


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




