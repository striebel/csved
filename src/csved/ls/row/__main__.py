import sys
import argparse 
import textwrap


from . import ls_row


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



def init_parser(
    prclc : argparse._SubParsersAction = None
) -> argparse.ArgumentParser:
    if prclc is None:
        prclcr = argparse.ArgumentParser(**PRCLCRA)
    else:
        assert isinstance(prclc, argparse._SubParsersAction), type(prclc)
        prclcr = prclc.add_parser(NAME, **PRCLCRA)
    del prclc
    assert isinstance(prclcr, argparse.ArgumentParser), type(prclcr)
    
    prclcr.add_argument(
        '-i',
        '--row-idx',
        dest    = 'row_idx',
        metavar = 'row_idx',
        type    = int,
        default = None,
    )
    prclcr.add_argument(
        'csv_file_path',
        type = str,
    )
    prclcr.set_defaults(func=ls_row)
    
    return prclcr



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



