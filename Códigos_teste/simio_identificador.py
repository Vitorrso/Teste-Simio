def isSimian(dna):
    rows = len(dna)
    cols = len(dna[0]) if rows > 0 else 0

    def check_sequence(seq):
        return any(seq.count(ch * 4) > 0 for ch in "ATCG")

    # Verifica sequências nas linhas
    for row in dna:
        if check_sequence(row):
            return True

    # Verifica sequências nas colunas
    for col in range(cols):
        column_sequence = ''.join(dna[row][col] for row in range(rows))
        if check_sequence(column_sequence):
            return True

    # Verifica sequências nas diagonais principal e secundária
    for start_row in range(rows - 3):
        for start_col in range(cols - 3):
            main_diag = ''.join(dna[start_row + i][start_col + i] for i in range(4))
            anti_diag = ''.join(dna[start_row + i][start_col + 3 - i] for i in range(4))
            if check_sequence(main_diag) or check_sequence(anti_diag):
                return True

    return False
