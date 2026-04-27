# Matriz com os dados dos alunos
prontuarioAlunos = [
    [970, "Hamilton", "TI", 7, 8, 11],
    [970, "Hamilton", "DS", 5, 2, 10],
    [970, "Hamilton", "Comunicação", 4, 4, 4]
]

# Função para calcular média
def calculaMedia(escolhido):
    media = sum(prontuarioAlunos[escolhido][3:])
    media /= len(prontuarioAlunos[escolhido][3:])
    return media

# Item 4: Função agora aceita um parâmetro "nomeFiltro"
# Se nomeFiltro for "None", ela processa todos (para a opção 3 do menu)
def identificaAprovados(nomeFiltro=None):
    listaDeResultados = []
    for aluno in range(len(prontuarioAlunos)):
        nome_atual = prontuarioAlunos[aluno][1]
        
        # Filtro: Se estivermos buscando um nome e ele não for o atual, pula
        if nomeFiltro != None and nome_atual != nomeFiltro:
            continue
            
        mediaDisciplina = calculaMedia(aluno)
        if mediaDisciplina >= 6:
            listaDeResultados.append([nome_atual, prontuarioAlunos[aluno][2], "aprovado", mediaDisciplina])
        else:
            listaDeResultados.append([nome_atual, prontuarioAlunos[aluno][2], "reprovado", mediaDisciplina])
    return listaDeResultados

# Item 2: Correção da variável alunoEncontrado (removido o else que resetava o status)
def relatorioDesempenho(nomeAluno):
    # Passamos o nome para a função processar apenas o necessário
    listaRelatorio = identificaAprovados(nomeAluno)
    alunoEncontrado = False 
    
    for item in listaRelatorio:
        # Se entrar aqui, sabemos que o nome coincide
        print(f"O aluno {item[0]} foi {item[2]} na disciplina {item[1]} com uma média de {item[3]}")
        alunoEncontrado = True
            
    if not alunoEncontrado:
        print("Aluno não localizado, verifique o nome informado e tente novamente")

# --- FUNÇÕES ORIGINAIS PRESERVADAS ---

def adicionarAluno():
    prontuarioAlunos.append([int(input("digite o código do aluno  ")), input("digite o primeiro nome do aluno do aluno  "), input("digite a disciplina  "), int(input("digite a nota da primeira avaliação  ")),int(input("digite a nota da segunda avaliação  ")), int(input("digite a nota da terceira avaliação  ")) ])
    print("Aluno Adicionado com sucesso")
    print(f"Nome: {prontuarioAlunos[len(prontuarioAlunos)-1][1]}")
    print(f"Código do aluno: {prontuarioAlunos[len(prontuarioAlunos)-1][0]}")
    print(f"Disciplina: {prontuarioAlunos[len(prontuarioAlunos)-1][2]}")
    print(f"Notas: {prontuarioAlunos[len(prontuarioAlunos)-1][3:]}")

def menuNavegacao():
    print("*" * 60)
    print("Digite o número correspondente a uma das funções abaixo:")
    print("1 - Cadastrar Aluno(a)")
    print("2 - Relatório de Desempenho")
    print("3 - Lista Completa de Aprovados")
    print("4 - Sair do Programa")

    escolherFuncao = int(input("Qual opção vc deseja?"))
    match escolherFuncao:
        case 1:
            print(" " * 60)
            adicionarAluno()
            menuNavegacao()
        case 2:
            print(" " * 60)
            relatorioDesempenho(input("Diigite o nome do aluno"))
            menuNavegacao()
        case 3:
            print(" " * 60)
            # Chama a função sem filtro para listar todos
            listaResultados = identificaAprovados()
            print(listaResultados)
            menuNavegacao()
        case 4:
            print(" " * 60)
            print("Obrigado e volte sempre!")
            return
        case _:
            print(" " * 60)
            print("Seleção inválida")
            menuNavegacao()

menuNavegacao()
