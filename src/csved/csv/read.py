import os
import sys
import textwrap



def read_csv_file(csv_file_path) -> list:
    '''
    A csv file has two primary special characters:
    newlines (\\n) to delimit rows and commas (,) to delimit cells
    within a row.
    If it is desired that a cell contain one, or both, of the
    special characters, the special characters are encoded within the cell
    like any other character without any kind of escape syntax.
    However, the entire cell is enclosed in double quote characters (")
    so that when a comma or newline is scanned before reaching the
    cell-ending double quote character, the reader knows that those characters
    should be included in the cell like any other character and do not mark
    the end of a cell or the end of a row.
    The only complication that doing this introduces is that it makes
    the double quote character itself a special character.
    If a double quote character were to be the first regular character in
    a cell, this would introduce ambiguity as to whether the double quote
    should be interpreted as introducing a special double-quoted cell that contains
    commas and/or newlines or whether the double quote should be interpreted
    as an ordinary character like any other that is included in the cell.
    This ambiguity is resolved by requiring all double quotes that appear in a
    cell to be escaped by being duplicated, so one double quote (") is replaced
    by two ("").
    And any cell that contains a double quote that has been escaped must be wrapped
    in double quotes the same as a cell that contains a comma or a newline.
    '''

    assert os.path.isfile(csv_file_path), csv_file_path

    with open(csv_file_path, 'rt') as csv_file:
        csv_str = csv_file.read()
    del csv_file_path, csv_file
    
    
    STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR              = 'state_begin_cell_read_first_decision_char'
    STATE_BEGIN_CELL_READ_SECOND_DECISION_CHAR             = 'state_begin_cell_read_second_decision_char'
    STATE_BEGIN_CELL_READ_THIRD_DECISION_CHAR              = 'state_begin_cell_read_third_decision_char'

    STATE_CONTINUE_UNQUOTED_CELL_READ                      = 'state_continue_unquoted_cell_read'
    STATE_CONTINUE_UNQUOTED_CELL_READ_SECOND_DECISION_CHAR = 'state_continue_unquoted_cell_read_second_decision_char'

    STATE_CONTINUE_QUOTED_CELL_READ                        = 'state_continue_quoted_cell_read'
    STATE_CONTINUE_QUOTED_CELL_READ_SECOND_DECISION_CHAR   = 'state_continue_quoted_cell_read_second_decision_char'
    STATE_CONTINUE_QUOTED_CELL_READ_THIRD_DECISION_CHAR    = 'state_continue_quoted_cell_read_third_decision_char'
    STATE_CONTINUE_QUOTED_CELL_READ_FOURTH_DECISION_CHAR   = 'state_continue_quoted_cell_read_fourth_decision_char'

    STATE_EOF                                              = 'state_eof'

    state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

    rows = [[]]

    i = 0
    while i < len(csv_str):

        if STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR == state:

            if '"' == csv_str[i]:

                state = STATE_BEGIN_CELL_READ_SECOND_DECISION_CHAR

            elif ',' == csv_str[i]:

                rows[-1].append('')

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

            elif '\n' == csv_str[i]:

                rows[-1].append('')

                rows.append([])

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

            else:
                assert csv_str[i] not in ('"', ',', '\n')

                rows[-1].append(csv_str[i])

                state = STATE_CONTINUE_UNQUOTED_CELL_READ

        elif STATE_BEGIN_CELL_READ_SECOND_DECISION_CHAR == state:

            assert '"' == csv_str[i-1]

            if '"' == csv_str[i]:

                if i + 1 == len(csv_str):

                    rows[-1].append('"')

                    state = STATE_EOF

                else:

                    state = STATE_BEGIN_CELL_READ_THIRD_DECISION_CHAR

            else:
                assert '"' != csv_str[i]

                assert csv_str[i] not in (',', '\n')
               
                rows[-1].append(csv_str[i])

                state = STATE_CONTINUE_QUOTED_CELL_READ

        elif STATE_BEGIN_CELL_READ_THIRD_DECISION_CHAR == state:

            assert '"' == csv_str[i-2]
            assert '"' == csv_str[i-1]

            if '"' == csv_str[i]:

                rows[-1].append('"')

                state = STATE_CONTINUE_QUOTED_CELL_READ

            else:
                assert '"' != csv_str[i]

                if ',' == csv_str[i]:

                    rows[-1].append('"')

                    state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

                elif '\n' == csv_str[i]:

                    rows[-1].append('"')

                    rows.append([])
                    
                    state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

                else:
                    assert csv_str[i] not in ('"', ',', '\n')

                    rows[-1].append('"')

                    rows[-1][-1] += csv_str[i]

                    state = STATE_CONTINUE_UNQUOTED_CELL_READ

        elif STATE_CONTINUE_UNQUOTED_CELL_READ == state:

            if '"' == csv_str[i]:

                state = STATE_CONTINUE_UNQUOTED_CELL_READ_SECOND_DECISION_CHAR

            elif ',' == csv_str[i]:

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

            elif '\n' == csv_str[i]:

                rows.append([])

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

            else:
                rows[-1][-1] += csv_str[i]

                state = STATE_CONTINUE_UNQUOTED_CELL_READ

        elif STATE_CONTINUE_UNQUOTED_CELL_READ_SECOND_DECISION_CHAR == state:

            assert '"' == csv_str[i-1]

            assert '"' == csv_str[i]

            rows[-1][-1] += '"'

            state = STATE_CONTINUE_UNQUOTED_CELL_READ

        elif STATE_CONTINUE_QUOTED_CELL_READ == state:

            if '"' == csv_str[i]:

                if i + 1 == len(csv_str):

                    state = STATE_EOF

                else:
                    state = STATE_CONTINUE_QUOTED_CELL_READ_SECOND_DECISION_CHAR

            else:
                assert '"' != csv_str[i]

                rows[-1][-1] += csv_str[i]

                state = STATE_CONTINUE_QUOTED_CELL_READ

        elif STATE_CONTINUE_QUOTED_CELL_READ_SECOND_DECISION_CHAR == state:

            assert '"' == csv_str[i-1]

            if '"' == csv_str[i]:

                state = STATE_CONTINUE_QUOTED_CELL_READ_THIRD_DECISION_CHAR

            elif ',' == csv_str[i]:

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

            else:
                assert '\n' == csv_str[i]

                rows.append([])

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

        elif STATE_CONTINUE_QUOTED_CELL_READ_THIRD_DECISION_CHAR == state:

            assert '"' == csv_str[i-2]
            assert '"' == csv_str[i-1]

            if '"' == csv_str[i]:

                state = STATE_CONTINUE_QUOTED_CELL_READ_FOURTH_DECISION_CHAR

            else:
                rows[-1][-1] += '"'
                rows[-1][-1] += csv_str[i]

                state = STATE_CONTINUE_QUOTED_CELL_READ

        elif STATE_CONTINUE_QUOTED_CELL_READ_FOURTH_DECISION_CHAR == state:

            assert '"' == csv_str[i-3]
            assert '"' == csv_str[i-2]
            assert '"' == csv_str[i-1]

            if '"' == csv_str[i]:

                rows[-1][-1] += '"'

                state = STATE_CONTINUE_QUOTED_CELL_READ_SECOND_DECISION_CHAR

            elif ',' == csv_str[i]:

                rows[-1][-1] += '"'

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR

            else:
                assert '\n' == csv_str[i]
                
                rows[-1][-1] += '"'

                rows.append([])

                state = STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR
        else:
            raise RuntimeError(f'unexpected state "{state}"')
        i += 1


    assert i == len(csv_str), (i, len(csv_str))
    del i, csv_str

    if STATE_EOF == state:
        assert len(rows[0]) == len(rows[-1]), (len(rows[0]), len(rows[-1]))
        pass

    else:
        assert STATE_BEGIN_CELL_READ_FIRST_DECISION_CHAR == state, state
        assert [] == rows[-1], len(rows[-1])
        assert [] == rows.pop(-1)
        pass
        
    del state


    assert 0 < len(rows), len(rows)


    first_row_width = len(rows[0])

    for row_idx, row in enumerate(rows[1:], start=1):

        if len(row) != first_row_width:

            raise ValueError(
                textwrap.dedent(
                    f'''\
                    The row with row_idx=0 in the csv file contains {first_row_width} cells,
                        but the row with row_idx={row_idx} contains {len(row)}:
                            rows[0]: {rows[0]}
                            rows[{row_idx}]: {rows[row_idx]}'''
                )
            ) 
    
    return rows
            





