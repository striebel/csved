import os
import sys
import textwrap

from ...csv.read import read_csv_file
from ...csv.write import write_csv_file


def cp_row(src_rowidx: int, dst_rowidx: int, csv_file_path: str) -> int:
    
    assert isinstance(src_rowidx, int), type(src_rowidx)
    assert isinstance(dst_rowidx, int), type(dst_rowidx)
    assert src_rowidx != dst_rowidx, (src_rowidx, dst_rowidx)
    
    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path
    
    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)
    
    src_row = rows[src_rowidx]
    src_row_is_not_empty = False
    
    for col in src_row:
        assert isinstance(col, str), type(col)
        if 0 < len(col):
            src_row_is_not_empty = True
    del src_row

    src_row_is_empty = not src_row_is_not_empty
    del src_row_is_not_empty

    if src_row_is_empty:
        sys.stdout.write(
            textwrap.dedent(
                f'''\
                Error: The row at src_rowidx={src_rowidx} is empty:
                Use "insert" to create an empty row, not "cp"'''
            ).replace('\n', ' ') + '\n'
        )
        return 1
    del src_row_is_empty
    
    
    dst_row = rows[dst_rowidx]
    dst_row_is_not_empty = False

    for col in dst_row:
        assert isinstance(col, str), type(col)
        if 0 < len(col):
            dst_row_is_not_empty = True
    del dst_row


    if dst_row_is_not_empty:
        sys.stdout.write(
            textwrap.dedent(
                f'''\
                Error: The row at dst_rowidx={dst_rowidx} is not empty
                and clobbering is disallowed:
                Instead, you must first "delete" the row, then "insert" an empty row,
                then "cp" over the empty row'''
            ).replace('\n', ' ') + '\n'
        )
        return 1 
    del dst_row_is_not_empty 


    assert src_rowidx != dst_rowidx
    ncols = len(rows[0])
    assert ncols == len(rows[src_rowidx])
    assert ncols == len(rows[dst_rowidx])
    for j in range(ncols):
        assert '' == rows[dst_rowidx][j]
        rows[dst_rowidx][j] = rows[src_rowidx][j]
    del ncols, src_rowidx, dst_rowidx


    assert write_csv_file(rows=rows, csv_file_path=csv_file_path) is None
    del rows, csv_file_path

    return 0





