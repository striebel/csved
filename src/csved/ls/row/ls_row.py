import sys
import os

from ...csv.read import read_csv_file



def ls_rows(rows: list) -> int:

    rowidxs_str = ''
    for rowidx in range(1, len(rows)):
        if 0 < len(rowidxs_str):
            rowidxs_str += ' '
        rowidxs_str += str(rowidx)
    
    rowidxs_str += '\n'
    sys.stdout.write(rowidxs_str)
    
    return 0



def show_row(
    rows   : list,
    rowidx: int,
) -> int:
    assert isinstance(rows, list), type(rows)
    assert 2 <= len(rows), len(rows)

    assert isinstance(rowidx, int), type(rowidx)
    assert (
        ( -(len(rows)-1) <= rowidx and rowidx <= -1 )
        or
        ( 1 <= rowidx and rowidx < len(rows) )
    ), (rowidx, len(rows))


    colidx_to_fieldname = \
        {
            colidx: fieldname
            for colidx, fieldname in enumerate(rows[0])
        }


    colidx__fieldname = \
        [
            (colidx, fieldname)
            for colidx, fieldname in colidx_to_fieldname.items()
        ]

    colidx__fieldname.sort(reverse=False)


    fields = \
        {
            colidx_to_fieldname[colidx]: fieldvalue
            for colidx, fieldvalue in enumerate(rows[rowidx])
        }


    max_fieldname_width = max(len(fieldname) for fieldname in fields.keys())

    a = 'fieldname'.ljust(max_fieldname_width)
    b = '---------'.ljust(max_fieldname_width)

    sys.stdout.write(f'colidx{" "*2}{a}{" "*2}fieldvalue\n')
    sys.stdout.write(f'------{" "*2}{b}{" "*2}----------\n')

    del a, b

    for colidx, fieldname in colidx__fieldname:

        # ci: colidx
        ci = str(colidx).rjust(6)
        del colidx

        # fv: fieldvalue
        fv = str(fields[fieldname])

        # fn: fieldname
        fn = fieldname.ljust(max_fieldname_width)
        del fieldname

        width = 6 + 2 + max_fieldname_width + 2

        try:
            # fvl: fieldvalue list
            fvl = fv.split()
        except AttributeError as ae:
            sys.stderr.write(
                textwrap.dedent(
                    f'''\
                    ci: "{ci}"
                    fv: "{fv}"
                    fn: "{fn}"
                    '''
                )
            )
            sys.exit(2)

        assert ''.split() == []

        sys.stdout.write(f'{ci}{" "*2}{fn}{" "*2}')

        if [] == fvl:
            sys.stdout.write('\n')
            continue
        
        # wi: word index
        # li: line index
        wi_to_li = {0: 0}
        
        # cli: current line index
        # cll: current line length
        cli = 0
        cll = width + len(fvl[0])

        for wi, w in enumerate(fvl[1:], start=1):
            if 80 <= cll + 1 + len(w):
                cli += 1
                cll = width + len(w)
                assert wi not in wi_to_li, wi
                wi_to_li[wi] = cli
            else:
                assert cll + 1 + len(w) < 80

                cll = cll + 1 + len(w)
                wi_to_li[wi] = cli
        
        # li_to_l: line index to line
        li_to_l = dict()
        for wi, li in wi_to_li.items():
            if li not in li_to_l:
                li_to_l[li] = []
            li_to_l[li].append(fvl[wi])
        
        for li, l in li_to_l.items():
            # ls: line str
            ls = ' '.join(l)
            if 0 < li:
                sys.stdout.write(f'{" "*width}')
            sys.stdout.write(f'{ls}\n')
        

    return 0
    


def ls_row(
    rowidx       : int,
    csv_file_path: str,
) -> int:
    '''\
    List rows in a csv file to stdout.
    
    :param rowidx: The specific row to show in detail.
    :param csv_file_path: Path to the csv file which should have its rows listed.
    
    :return: exit status
    '''
    assert isinstance(rowidx, int), type(rowidx)

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path
    
    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    
    if rowidx is None:
        exit_status = ls_rows(rows=rows)
    else:
        assert isinstance(rowidx, int), type(rowidx)
        exit_status = show_row(rows=rows, rowidx=rowidx)

    assert isinstance(exit_status, int), type(exit_status)
    assert 0 <= exit_status and exit_status <= 255, exit_status

    return exit_status





