import os
import sys
import textwrap
import time
import subprocess

from ...csv.read import read_csv_file
from ...csv.write import write_csv_file



def ed_row(rowidx: int, csv_file_path: str) -> int:

    assert isinstance(rowidx, int), type(rowidx)

    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)
    assert os.path.isfile(csv_file_path), csv_file_path
    assert 0 < os.path.getsize(csv_file_path), csv_file_path

    rows = read_csv_file(csv_file_path=csv_file_path)
    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)

    column_names = rows[0]

    row_to_edit = rows[rowidx]
    
    
    tmp_dir_path = '/tmp'
    assert os.path.isdir(tmp_dir_path), tmp_dir_path

    # sste: seconds since the epoch
    sste = time.time()
    assert isinstance(sste, float), type(sste)
    sste = round(sste)
    assert isinstance(sste, int), type(sste)
    
    tmp_subdir_name = f'csved.{sste}'
    del sste
    
    tmp_subdir_path = os.path.join(tmp_dir_path, tmp_subdir_name)
    del tmp_dir_path, tmp_subdir_name
    
    assert not os.path.isdir(tmp_subdir_path), tmp_subdir_path
    os.mkdir(tmp_subdir_path, mode=0o700)
    
    tmp_file_name = 'tmp_file.txt'
    tmp_file_path = os.path.join(tmp_subdir_path, tmp_file_name)
    del tmp_subdir_path, tmp_file_name
    assert not os.path.isfile(tmp_file_path)
    
    
    tmp_file_str = ''
    assert len(column_names) == len(row_to_edit), (len(column_names), len(row_to_edit))
    for colidx, (colname, colvalue) in enumerate(zip(column_names, row_to_edit)):
        assert isinstance(colname, str), type(colname)
        assert isinstance(colvalue, str), type(colvalue)
        tmp_file_str += f'# colidx={colidx}; colname={colname}\n'
        
        colvalue = ' '.join( colvalue.split() )
        
        if len(colvalue) <= 70:
            tmp_file_str += colvalue + '\n'
        else:
            assert 70 < len(colvalue)
            
            lines = textwrap.wrap(text=colvalue, width=70)
            assert isinstance(lines, list), type(lines)
            assert 0 < len(lines)
            
            for line in lines:
                tmp_file_str += line + '\n'

        tmp_file_str += '\n'

    del column_names, row_to_edit

    assert 0 < len(tmp_file_str)
    assert not os.path.isfile(tmp_file_path), tmp_file_path
    with open(tmp_file_path, 'wt') as tmp_file:
        tmp_file.write(tmp_file_str)
    del tmp_file
    
    # open vim and wait for the user to exit
    subprocess.call(['vim', tmp_file_path])
    
    with open(tmp_file_path, 'rt') as tmp_file:
        updated_tmp_file_str = tmp_file.read()
    del tmp_file
    
    
    assert os.path.isfile(tmp_file_path), tmp_file_path
    tmp_subdir_path = os.path.dirname(tmp_file_path)
    os.unlink(tmp_file_path)
    assert not os.path.isfile(tmp_file_path), tmp_file_path
    del tmp_file_path

    assert os.path.isdir(tmp_subdir_path), tmp_subdir_path
    os.rmdir(tmp_subdir_path)
    assert not os.path.isdir(tmp_subdir_path), tmp_subdir_path
    del tmp_subdir_path


    if updated_tmp_file_str == tmp_file_str:
        sys.stderr.write('No changes detected: Aborting\n')
        return 1
    del tmp_file_str
    sys.stderr.write('Changes detected: Processing ... ')
    
    
    assert isinstance(updated_tmp_file_str, str), type(updated_tmp_file_str)
    assert 0 < len(updated_tmp_file_str)
    lines = updated_tmp_file_str.split('\n')
    del updated_tmp_file_str
    assert isinstance(lines, list), type(lines)
    assert 0 < len(lines)
    
    
    STATE_SEEK_NEXT_COLUMN  = 'state_seek_next_column'
    STATE_READ_COLUMN_VALUE = 'state_read_column_value'

    state = STATE_SEEK_NEXT_COLUMN

    colidx = -1

    updated_row = [''] * len(rows[0])

    for line in lines:

        if STATE_SEEK_NEXT_COLUMN == state:

            if '' == line.strip():

                pass

            else:
                assert f'# colidx={colidx+1}; colname={rows[0][colidx+1]}' == line, line

                colidx += 1

                state = STATE_READ_COLUMN_VALUE

        elif STATE_READ_COLUMN_VALUE == state:

            if '' == line.strip():

                state = STATE_SEEK_NEXT_COLUMN

            elif (
                colidx + 1 < len(rows[0])
                and
                f'# colidx={colidx+1}; colname={rows[0][colidx+1]}' == line
            ):

                colidx += 1

                state = state

            else:
                assert 0 < len(line.strip())

                updated_row[colidx] += ' ' + line
    
    assert STATE_SEEK_NEXT_COLUMN == state, state
    del state
    
    assert colidx + 1 == len(rows[0]), (colidx, len(rows[0]))
    del colidx
    
    updated_row = [ ' '.join( col.split() ) for col in updated_row ]
    
    assert len(updated_row) == len(rows[0])
    assert len(updated_row) == len(rows[rowidx])
    
    for colidx in range(len(rows[0])):
        rows[rowidx][colidx] = updated_row[colidx]
    del updated_row
    
    sys.stderr.write('Done\n')
    sys.stderr.write('Saving ... ')
    
    assert write_csv_file(rows=rows, csv_file_path=csv_file_path) is None
    del rows, csv_file_path

    sys.stderr.write('Done\n')
    
    
    return 0







