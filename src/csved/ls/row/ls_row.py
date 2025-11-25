import sys
import os

from ...csv.read import read_csv_file



def ls_row(
    csv_file_path: str,
) -> int:
    '''\
    List rows in a csv file to stdout.
    
    :param csv_file_path: Path to the csv file which should have its rows listed.
    
    :return: exit status
    '''
    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)

    row_idxs_str = ''
    for row_idx in range(1, len(rows)+1):
        if 0 < len(row_idxs_str):
            row_idxs_str += ' '
        row_idxs_str += str(row_idx)
    
    row_idxs_str += '\n'
    sys.stdout.write(row_idxs_str)

    return None



