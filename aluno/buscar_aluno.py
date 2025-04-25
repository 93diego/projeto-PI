def buscar_alunos(alunos):
    with open("inscricoes_aluno.txt", "r") as arquivo:

        for linha in arquivo:
            dados = linha.strip().split(",")
            print(f"Nome: {dados[0]}, Idade: {dados[1]}, Modalidade: {dados[2]}")
