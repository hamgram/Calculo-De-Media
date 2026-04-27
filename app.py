""" Calcular médias das disciplinas
Identificar alunos aprovados ou reprovados
Gerar um relatório simples de desempenho """

# Matriz com os dados dos alunos sendo eles: código do aluno, nome, disciplina, notas

prontuarioAlunos = [
    [970, "Hamilton", "TI", 7, 8, 11],
    [970,"Hamilton", "DS", 5, 2, 10 ],
    [970, "Hamilton","Comunicação", 4, 4, 4 ]
]
 
# Função para calcular média da disciplina, retorna media por disciplina

def calculaMedia(escolhido):
    media = sum(prontuarioAlunos[escolhido][3:])
    media /= len(prontuarioAlunos[escolhido][3:])
    return media

# Função para identificar alunos aprovados ou reprovados
def identificaAprovados():
    listaDeResultados = []
    for aluno in range(len(prontuarioAlunos)):
        mediaDisciplina = calculaMedia(aluno)
        if mediaDisciplina >= 6:
            listaDeResultados.append([prontuarioAlunos[aluno][1],prontuarioAlunos[aluno][2],"aprovado", mediaDisciplina])
        else:
            listaDeResultados.append([prontuarioAlunos[aluno][1],prontuarioAlunos[aluno][2],"reprovado", mediaDisciplina])
    return listaDeResultados
            

# Função para gerar relatório de desempenho
listaRelatorio = identificaAprovados()
nomeAluno = "Hamilton"
for item in listaRelatorio:
    if item[0] == nomeAluno:
        print(f"O aluno {item[0]} foi {item[2]} na disciplina {item[1]} com uma média de {item[3]}")



#print(identificaAprovados())
#print(calculaMedia(int((input("Qual o número do aluno?")))))