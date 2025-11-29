import os
import sys
import textwrap


from ...csv.read import read_csv_file
from ...csv.write import write_csv_file



def delete_col(colidx: int, csv_file_path) -> int:
    
    assert isinstance(colidx, int), type(colidx)

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)

    colname = rows[0][colidx]
    col_to_delete = [row[colidx] for row in rows]
    assert len(rows) == len(col_to_delete)

    col_to_delete_is_not_empty = False

    for cell in col_to_delete:
        assert isinstance(cell, str), type(cell)
        if 0 < len(cell):
            col_to_delete_is_not_empty = True

    if col_to_delete_is_not_empty:
        yorn = \
            input(
                textwrap.dedent(
                    f'''\
                    The col at colidx={colidx} (which has colname="{colname}") is nonempty;
                        are you sure you want to delete it? [y/n]> '''
                )
            )
        if 'y' != yorn:
            sys.stderr.write(f'You entered "{yorn}": Aborting\n')
            return 1

    deleted_col = []
    for row in rows:
        deleted_col.append( row.pop(colidx) )

    assert col_to_delete == deleted_col
    del col_to_delete, deleted_col

    assert write_csv_file(rows=rows, csv_file_path=csv_file_path) is None
    del rows, csv_file_path

    sys.stderr.write(f'Column at colidx={colidx} was deleted\n')
    del colidx

    return 0




