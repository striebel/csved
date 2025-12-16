import sys
import os

from ...csv.read import read_csv_file


def ls_col(csv_file_path: str) -> int:
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



