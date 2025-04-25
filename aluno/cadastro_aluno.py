def geral1(alunos):

    def cadastrar_inscricao(nome_aluno, idade, modalidade):
        with open("inscricoes_aluno.txt", "a") as arquivo:
            linha = f"{nome_aluno},{idade},{modalidade}\n"
            arquivo.write(linha)
        print(" Inscrição cadastrada com sucesso!")

    nome_aluno = input(" Digite o nome do aluno: ")
    idade = int(input(" Digite a idade: "))
    modalidade = str(input(" Digite a modalidade do aluno:"))
    cadastrar_inscricao(nome_aluno, idade, modalidade)


def listar_inscricoes():
    with open("inscricoes_aluno.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            print(f" Aluno: {dados[0]} | Idade: {dados[1]} | Modalidade: {dados[2]}")
