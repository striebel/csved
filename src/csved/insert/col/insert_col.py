import os


from ...csv.read import read_csv_file
from ...csv.write import write_csv_file



def insert_col(colidx: int, colname: str, csv_file_path: str) -> int:
    
    assert isinstance(colidx, int), type(colidx)
    
    assert isinstance(colname, str), type(colname)
    
    assert isinstance(csv_file_path, str)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path
    
    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)
    
    rows[0].insert(colidx, colname)
    for i in range(1, len(rows)):
        rows[i].insert(colidx, '')
    
    assert write_csv_file(rows=rows, csv_file_path=csv_file_path) is None
    del rows, csv_file_path

    return 0


    
