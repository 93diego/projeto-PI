from procurar_aluno import proc_aluno


def inserir_alu():
    nome_aluno = input("Digite o aluno que deseja inserir: ")

    aluno = proc_aluno(nome_aluno)

    if aluno:
        print("x")
