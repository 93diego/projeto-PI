def proc_aluno(nome):
    with open("inscricoes_aluno.txt", "r") as arquivo:
        for aluno in arquivo:
            if aluno[0].lower() == nome.lower():
                return aluno
    return None
