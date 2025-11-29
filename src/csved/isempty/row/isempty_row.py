import os
import sys


from ...csv.read import read_csv_file


def isempty_row(rowidx: int, csv_file_path: str) -> int:

    assert isinstance(rowidx, int), type(rowidx)

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)

    row_to_check = rows[rowidx]

    isempty = True
    for col in row_to_check:
        assert isinstance(col, str), type(col)
        if 0 < len(col):
            isempty = False

    if isempty is False:
        sys.stderr.write(f'row is NOT empty\n')
        return 1

    assert isempty is True
    sys.stderr.write('row IS empty\n')
    return 0
    



