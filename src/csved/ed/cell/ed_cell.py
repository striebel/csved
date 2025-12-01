import os

from ...csv.read import read_csv_file
from ...csv.write import write_csv_file



def ed_cell(rowidx: int, colidx: int, cellvalue: str, csv_file_path: str) -> int:

    assert isinstance(rowidx, int), type(rowidx)
    assert isinstance(colidx, int), type(colidx)
    assert isinstance(cellvalue, str), type(cellvalue)

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)

    row_to_update = rows[rowidx]

    return 0





