def geral1(alunos):

    def cadastrar_inscricao(nome_aluno, idade):
        with open("inscricoes_aluno.txt", "a") as arquivo:
            linha = f"{nome_aluno},{idade}\n"
            arquivo.write(linha)
        print("Inscrição cadastrada com sucesso!")

    def listar_inscricoes():
        with open("inscricoes_aluno.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                print(f"Aluno: {dados[0]} | Idade: {dados[1]}")

    nome_aluno = input("digite o nome do aluno: ")
    idade = int(input("digite a idade: "))
    cadastrar_inscricao(nome_aluno, idade)
