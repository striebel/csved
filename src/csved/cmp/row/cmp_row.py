import os
import sys

from ...csv.read import read_csv_file


def cmp_row(a_rowidx: int, b_rowidx: int, csv_file_path: str) -> int:

    assert isinstance(a_rowidx, int), type(a_rowidx)
    assert isinstance(b_rowidx, int), type(b_rowidx)
    assert a_rowidx != b_rowidx, (a_rowidx, b_rowidx)

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    del csv_file_path
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)

    a = rows[a_rowidx]
    b = rows[b_rowidx]
    del rows

    assert isinstance(a, list), type(a)
    assert isinstance(b, list), type(b)
    assert len(a) == len(b), (len(a), len(b))
    if a != b:
        sys.stderr.write('rows are NOT equal\n')
        return 1
 
    assert a == b
    sys.stderr.write('rows ARE equal\n')

    return 0




