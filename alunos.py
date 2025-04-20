from voltar_menu import menu_prin

alunos = []
menu_1 = []

def cad_alunos(alunos):
    nome = input("digite o nome do aluno: ")
    idade = int(input("digite a idade do aluno: "))
    alunos.append({"nome": nome, "idade": idade})
    print(f"aluno'{nome}' cadastrado")
    menu_prin(menu_1)

##cad_alunos()
##print(alunos)
    
