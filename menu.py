from busca_modalidade import buscar_modalidade
from aluno.buscar_aluno import buscar_alunos
from voltar_menu import menu_prin
from busca_idade import buscar_idade

menu_1 = []
modalidade = []
alunos = []
idade = []


def relatorios(relatorio_p):
    print("\n --- Relatórios ---")
    print(" 1. Alunos")
    print(" 2. Modalidades")
    print(" 3. Idades")
    print(" 4. Sair")
    opcao = int(input(" digite a opção desejada: "))

    if opcao == 1:
        buscar_alunos(alunos)
    elif opcao == 2:
        buscar_modalidade(modalidade)
    elif opcao == 3:
        buscar_idade(idade)
    elif opcao == 4:
        menu_prin(menu_1)
