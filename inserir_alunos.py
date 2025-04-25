from procurar_aluno import proc_aluno


def insere_aluno():
    nome_aluno = input(" Digite o aluno que deseja inserir: ")

    aluno = proc_aluno(nome_aluno)
    print("teste")
    modalidade = list(input(" Em que Modalidade deseja cadastrar o aluno?: "))
    modalidade.append(aluno)
    print(" Aluno cadastrado com sucesso em {modalidade}")
