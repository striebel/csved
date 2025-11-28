import os


from ...csv.read import read_csv_file
from ...csv.write import write_csv_file


def insert_row(row_idx: int, csv_file_path: str) -> int:

    assert isinstance(row_idx, int), type(row_idx)
    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(list)
    assert 0 < len(rows)

    ncols = len(rows[0])
    assert 0 < ncols

    new_row = [''] * ncols
    rows.insert(row_idx, new_row)

    assert write_csv_file(rows=rows, csv_file_path=csv_file_path) is None

    return 0


