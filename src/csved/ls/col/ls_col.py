import sys
import os

from ...csv.read import read_csv_file


def ls_col_headers(csv_file_path: str) -> int:
    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path
    
    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)
    
    colidx__fieldname = \
        [
            ('colidx', 'fieldname'),
            ('------', '---------'),
        ]
    for colidx, fieldname in enumerate(rows[0]):
        assert isinstance(colidx, int), type(colidx)
        assert 0 <= colidx, colidx
        assert isinstance(fieldname, str), (colidx, type(fieldname), fieldname)
        colidx__fieldname.append((str(colidx), fieldname))

    max_colidx_width    = max(len(ci) for ci, __ in colidx__fieldname)
    max_fieldname_width = max(len(fn) for __, fn in colidx__fieldname)

    for ci, fn in colidx__fieldname:
        _ci = ci.rjust(max_colidx_width   )
        _fn = fn.ljust(max_fieldname_width)
        sys.stdout.write(f'{_ci}{" "*2}{_fn}\n')

    return 0


def ls_col_distinct_values(colidx: int, csv_file_path) -> int:
    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)
    assert isinstance(rows[0], list), type(rows)
    assert 0 < len(rows[0])
    assert isinstance(rows[0][0], str), type(rows[0][0])

    fieldname = rows[0][colidx]
    assert isinstance(fieldname, str), type(fieldname)

    max_width = len(fieldname)

    values = []
    for row in rows[1:]:
        assert isinstance(row, list), type(row)
       
        value = row[colidx] 
        assert isinstance(value, str), type(value)
        if value not in values:
            values.append(value)
            if max_width < len(values):
                max_width = len(values)

    fn = fieldname.ljust(max_width)
    del fieldname
    
    # ul: underline
    ul = '-' * max_width

    sys.stdout.write(f'{fn}\n'); del fn
    sys.stdout.write(f'{ul}\n'); del ul

    for fv in values:
        fv = fv.strip()
        fv = fv.ljust(max_width)
        sys.stdout.write(f'{fv}\n')

    return 0



def ls_col(colidx: int, distinct: bool, csv_file_path: str) -> int:

    if colidx is not None:
        assert isinstance(colidx, int), type(colidx)

    assert distinct in (True, False), distinct

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path


    if colidx is None:
        exit_status = ls_col_headers(csv_file_path=csv_file_path)
    else:
        assert isinstance(colidx, int), type(colidx)
        
        if distinct is True:
            exit_status = \
                ls_col_distinct_values(
                    colidx        = colidx,
                    csv_file_path = csv_file_path,
                )
        else:
            assert distinct is False, distinct
            raise NotImplementedError('try passing -d/--distinct')

    assert isinstance(exit_status, int), type(exit_status)
    assert 0 <= exit_status and exit_status <= 255, exit_status

    return exit_status






