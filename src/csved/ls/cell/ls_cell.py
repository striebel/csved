import os
import sys

from ...csv.read import read_csv_file


def ls_cell(rowidx, colidx, csv_file_path) -> int:
    assert isinstance(rowidx, int), type(rowidx)
    assert isinstance(colidx, int), type(colidx)

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path), csv_file_path
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    del csv_file_path
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)

    row = rows[rowidx]
    del rows
    assert isinstance(row, list), type(row)
    assert 0 < len(row)

    cell = row[colidx]
    del row
    assert isinstance(cell, str), type(cell)

    sys.stdout.write(f'{cell}\n')
    del cell

    return 0



