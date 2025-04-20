from busca_modalidade import buscar
from aluno.buscar_aluno import buscar_a

menu_1 = []
teste = []
teste2 = []

def relatorios(relatorio_p):
    print("\n --- Relatórios ---")
    print("1. Alunos")
    print("2. Modalidades")
    print("3. Idades")
    print("4. Sair")
    opcao = int(input("digite a opção desejada: "))

    if opcao == 1:
        buscar_a(teste2)
    elif opcao == 2:
        buscar(teste)
        
