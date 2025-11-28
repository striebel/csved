import os
import textwrap

from ...csv.read import read_csv_file
from ...csv.write import write_csv_file


def delete_row(rowidx: int, csv_file_path: str) -> int:
    
    assert isinstance(rowidx, int), type(rowidx)
    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path
    
    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)
    
    ncols = len(rows[0])
    assert 0 < ncols
    
    row_for_deletion = rows[rowidx]
    row_is_not_empty = False
    
    assert ncols == len(row_for_deletion), (ncols, len(row_for_deletion))
    for colidx, col in enumerate(row_for_deletion):
        assert isinstance(col, str), (col, rowidx, colidx, type(col))
        
        if 0 < len(col):
            row_is_not_empty = True
    
    if row_is_not_empty:
        yorn = \
            input(
                textwrap.dedent(
                    f'''\
                    The row at rowidx={rowidx} is nonempty;
                    are you sure you want to delete it? [y/n]> '''
                ).replace('\n', ' ')
            )
        if 'y' != yorn:
            return 1
    
    assert row_for_deletion == rows.pop(rowidx)

    assert write_csv_file(rows=rows, csv_file_path=csv_file_path) is None

    return 0



