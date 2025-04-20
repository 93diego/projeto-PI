def proc_aluno (nome):
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None
