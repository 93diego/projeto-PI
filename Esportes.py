# importando as funções
from modalidade import cad_modalidade
from aluno.cadastro_aluno import geral1
import modalidade
from voltar_menu import menu_prin
from procurar_aluno import proc_aluno
from menu import relatorios
from inserir_alunos import insere_aluno


# lugar onde vai armazenar os dados durante o programa
modalidades = []
alunos = []
alunos_m = []
relatorio_p = []

# menu principal, ele roda constante
while True:

    def menu():
        print("\n ---- Controle Esportes ----")
        print(" 1. Cadastrar aluno")
        print(" 2. Relatório")
        print(" 3. Sair")

        opcao = int(input("\n Digite uma opção: "))

        if opcao == 1:
            geral1(alunos)
        elif opcao == 2:
           relatorios(relatorio_p) 
        elif opcao == 4:
            print("Programa finalizado")
            exit()
        else:
            print("Opção inválida")

    menu()
