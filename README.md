# Teste-Simios

Este projeto implementa uma solução para detectar se uma sequência de DNA pertence a um símio ou a um humano. Ele consiste em três níveis:

1. **Nível 1: Função isSimian**
   - Arquivo: `simio_identificador.py`
   - Descrição: Contém a função `isSimian`, que verifica se uma sequência de DNA pertence a um símio.

2. **Nível 2: API REST**
   - Arquivo: `simio_api.py`
   - Descrição: Implementa uma API REST usando Flask para receber sequências de DNA via POST e determinar se são de um símio. Também registra os resultados em um banco de dados MySQL.

3. **Nível 3: Banco de Dados e Estatísticas**
   - Arquivo: `simio_database.py`
   - Descrição: Adiciona funcionalidades para armazenar sequências de DNA no banco de dados MySQL e fornece um endpoint para obter estatísticas sobre as verificações de DNA realizadas.

## Pré-requisitos

- Python 3.x
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Vitorrso/Teste---Simios.git

## Instale as dependências:
   comando: pip install -r requirements.txt

## Execute o servidor Flask:
  - comando: python simio_api.py
  - Faça uma requisição POST para http://127.0.0.1:5000/simian com dados JSON:
     - {
     - "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
     - }
  - Obtenha estatísticas fazendo uma requisição GET para http://127.0.0.1:5000/stats.
