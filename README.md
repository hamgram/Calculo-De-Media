markdown_content = """# Sistema de Gestão Escolar - Prontuário de Alunos

Este projeto consiste em um sistema simples de gestão de notas e desempenho acadêmico desenvolvido em Python. Ele permite o cadastro de alunos, cálculo de médias e geração de relatórios de aprovação.

## 🚀 Funcionalidades

O sistema oferece as seguintes operações através de um menu interativo:

1.  **Cadastrar Aluno(a):** Adiciona novos registros à base de dados, incluindo código, nome, disciplina e três notas.
2.  **Relatório de Desempenho:** Busca um aluno pelo nome e exibe sua situação (aprovado/reprovado) em cada disciplina cadastrada.
3.  **Lista Completa de Aprovados:** Gera uma lista contendo o status de todos os alunos e disciplinas registrados no sistema.
4.  **Cálculo Automático de Média:** O sistema utiliza uma função dedicada para calcular a média aritmética das três avaliações.

## 🛠️ Detalhes Técnicos

### Estrutura de Dados
Os dados são armazenados em uma matriz (lista de listas) chamada `prontuarioAlunos`, seguindo o formato:
`[Código, Nome, Disciplina, Nota1, Nota2, Nota3]`

### Lógica de Aprovação
* **Média para Aprovação:** ≥ 6.0
* **Processamento de Filtros:** A função `identificaAprovados()` foi otimizada para funcionar tanto como um buscador individual quanto como um gerador de relatório global, dependendo dos parâmetros fornecidos.

## 📋 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Copie o código para um arquivo com a extensão `.py` (ex: `gestao_alunos.py`).
3. Execute o arquivo no seu terminal ou IDE favorita:
   ```bash
   python gestao_alunos.py
