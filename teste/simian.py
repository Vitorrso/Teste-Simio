def is_simian(dna):
    n = len(dna)
    
    # Função auxiliar para verificar se uma sequência contém 4 letras iguais
    def has_sequence(s):
        for i in range(len(s) - 3):
            if len(set(s[i:i+4])) == 1:
                return True
        return False
    
    # Verificação horizontal
    for i in range(n):
        if has_sequence(dna[i]):
            return True
    
    # Verificação vertical
    for j in range(n):
        if has_sequence(''.join(dna[i][j] for i in range(n))): # Corrigido para percorrer as linhas
            return True
    
    # Verificação diagonal principal
    for i in range(n - 3):
        if has_sequence(''.join(dna[i+k][k] for k in range(n - i))):
            return True
    for j in range(1, n - 3):
        if has_sequence(''.join(dna[k][j+k] for k in range(n - j))):
            return True
    
    # Verificação diagonal secundária
    for i in range(n - 3):
        if has_sequence(''.join(dna[i+k][n-1-k] for k in range(n - i))):
            return True
    for j in range(1, n - 3):
        if has_sequence(''.join(dna[k][n-1-j-k] for k in range(n - j))):
            return True
    
    return False
