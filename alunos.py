alunos = []

def cad_alunos():
    nome = input("digite o nome do aluno: ")
    idade = int(input("digite a idade do aluno: "))
    alunos.append({"nome": nome, "idade": idade})
    print(f"aluno'{nome}' cadastrado")
    #menu_prin()

cad_alunos()
print(alunos)
    
