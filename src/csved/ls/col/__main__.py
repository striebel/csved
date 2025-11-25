import sys
import argparse
import textwrap


from . import ls_col


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



def init_parser(
    prclc : argparse._SubParsersAction = None
) -> argparse.ArgumentParser:
    if prclc is None:
        prclcc = argparse.ArgumentParser(**PRCLCCA)
    else:
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



def main() -> int:
    # pr: parser root
    pr = init_parser()
    assert isinstance(pr, argparse.ArgumentParser), type(pr)
    assert PROG == pr.prog, (PROG, pr.prog)
    
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





