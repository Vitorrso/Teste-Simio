# Teste-Simios

Este projeto implementa uma solução para detectar se uma sequência de DNA pertence a um símio ou a um humano. Ele consiste em três níveis:

1. **Nível 1: Função is_simian**
   - Arquivo: `simian.py`
   - Descrição: Contém a função `is_simian`, que verifica se uma sequência de DNA pertence a um símio.

2. **Nível 2: API REST**
   - Arquivo: `api.py`
   - Descrição: Implementa uma API REST usando Flask para receber sequências de DNA via POST e determinar se são de um símio. Também registra os resultados em um banco de dados SQLite.

3. **Nível 3: Banco de Dados e Estatísticas**
   - Arquivo: `simiandb.py`
   - Descrição: Adiciona funcionalidades para armazenar sequências de DNA no banco de dados SQLite e fornece um endpoint para obter estatísticas sobre as verificações de DNA realizadas.

## Pré-requisitos

- Python 3.x
- Flask 3.0.2
- SQLite 3.45.1

## Instale as dependências:
   instale todos os pré-requesitos

## Execute o servidor Flask:
  - comando: python api.py
  - Faça uma requisição POST para http://127.0.0.1:5000/simian com dados JSON:
     - {
     - "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
     - }
  - Obtenha estatísticas com a contagem de simios, contagem de humanos e a proporção entre eles fazendo uma requisição GET para http://127.0.0.1:5000/stats.
