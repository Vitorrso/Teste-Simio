import sqlite3

# Criar banco de dados e tabela
conn = sqlite3.connect('dna_database.db',check_same_thread= False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS dna (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sequence TEXT UNIQUE,
                    is_simian BOOLEAN
                )''')
conn.commit()

# Função para inserir um DNA na tabela
def insert_dna(sequence, is_simian):
    cursor.execute('INSERT OR IGNORE INTO dna (sequence, is_simian) VALUES (?, ?)', (sequence, is_simian))
    conn.commit()

# Função para obter estatísticas
def get_stats():
    cursor.execute('SELECT COUNT(CASE WHEN is_simian THEN 1 END), COUNT(CASE WHEN NOT is_simian THEN 1 END) FROM dna')
    simian_count, human_count = cursor.fetchone()
    return {'count_mutant_dna': simian_count, 'count_human_dna': human_count, 'ratio': simian_count / (simian_count + human_count)}
