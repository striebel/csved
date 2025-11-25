import sys
import os

from ...csv.read import read_csv_file



def ls_rows(rows: list) -> int:

    row_idxs_str = ''
    for row_idx in range(1, len(rows)+1):
        if 0 < len(row_idxs_str):
            row_idxs_str += ' '
        row_idxs_str += str(row_idx)
    
    row_idxs_str += '\n'
    sys.stdout.write(row_idxs_str)
    
    return 0



def show_row(
    rows   : list,
    row_idx: int,
) -> int:
    assert isinstance(rows, list), type(rows)
    assert 2 <= len(rows), len(rows)

    assert isinstance(row_idx, int), type(row_idx)
    assert (
        ( -(len(rows)-1) <= row_idx and row_idx <= -1 )
        or
        ( 1 <= row_idx and row_idx < len(rows) )
    ), (row_idx, len(rows))


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
            for colidx, fieldvalue in enumerate(rows[row_idx])
        }


    max_fieldname_width = max(len(fieldname) for fieldname in fields.keys())

    a = 'fieldname'.ljust(max_fieldname_width)

    sys.stdout.write(f'colidx{" "*2}{a}{" "*2}fieldvalue\n')

    del a

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
    row_idx      : int,
    csv_file_path: str,
) -> int:
    '''\
    List rows in a csv file to stdout.
    
    :param row_idx: The specific row to show in detail.
    :param csv_file_path: Path to the csv file which should have its rows listed.
    
    :return: exit status
    '''
    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path
    
    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    
    if row_idx is None:
        exit_status = ls_rows(rows=rows)
    else:
        assert isinstance(row_idx, int), type(row_idx)
        exit_status = show_row(rows=rows, row_idx=row_idx)

    assert isinstance(exit_status, int), type(exit_status)
    assert 0 <= exit_status and exit_status <= 255, exit_status

    return exit_status





