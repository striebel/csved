


def write_csv_file(rows: list, csv_file_path: str) -> None:

    assert isinstance(rows, list), type(rows)
    assert 0 < len(rows)
    assert isinstance(csv_file_path, str), type(csv_file_path)
    assert 0 < len(csv_file_path)

    ncols = len(rows[0])
    for rowidx in range(len(rows)):
        assert isinstance(rows[rowidx], list), (rowidx, type(rows[rowidx]))
        assert ncols == len(rows[rowidx]), (ncols, rowidx, len(rows[rowidx]))
        for colidx in range(len(ncols)):
            assert isinstance(rows[rowidx][colidx], str), \
                (rowidx, colidx, type(rows[rowidx][colidx])

    csv_str = ''
    for row in rows:
        for colidx, col in enumerate(row):
            if (
                ',' in col
                or
                '\n' in col
                or
                '"' in col
            ):
                col = col.replace('"', '""')
                col = f'"{col}"'
            if 0 < colidx:
                csv_str += ','
            csv_str += col
        csv_str += '\n'

    with open(csv_file_path, 'wt') as csv_file:
        csv_file.write(csv_str)
    del csv_str, csv_file, csv_file_path

    return None



