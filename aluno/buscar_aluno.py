def buscar_alunos(alunos):
    with open("inscricoes_aluno.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha)
