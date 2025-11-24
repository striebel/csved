import sys
import argparse
import textwrap


from . import hello_main


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


def init_parser(
    prc : argparse._SubParsersAction = None
) -> argparse.ArgumentParser:
    if prc is None:
        prch = argparse.ArgumentParser(**PRCHA)
    else:
        assert isinstance(prc, argparse._SubParsersAction), type(prc)
        prch = prc.add_parser(NAME, **PRCHA)
    del prc
    assert isinstance(prch, argparse.ArgumentParser), type(prch)
    prch.set_defaults(func=hello_main)
    return prch


def main() -> int:
    pr = init_parser()
    assert isinstance(pr, argparse.ArgumentParser), type(pr)
    assert PROG == pr.prog, (PROG, pr.prog)
    
    args = pr.parse_args()
    assert isinstance(args, argparse.Namespace)
    args = vars(args)
    assert isinstance(args, dict)
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





