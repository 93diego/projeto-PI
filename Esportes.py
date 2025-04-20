#importando as funções 
from modalidade import cad_modalidade
from alunos import cad_alunos
from voltar_menu import menu_prin
from procurar_aluno import proc_aluno
from menu import relatorios

#lugar onde vai armazenar os dados durante o programa
modalidades = []
alunos = []
alunos_m = []
relatorio_p = []


#menu principal, ele roda constante
while True:
    def menu():
        print("\n ---- Controle Esportes ----")
        print("\n 1. Cadastrar modalidade")
        print(" 2. Cadastrar aluno")
        print(" 3. Inserir aluno em modalidade")
        print(" 4. relatório")
        print(" 5. sair")

        opcao = int(input("\n Digite uma opção: "))

        if opcao == 1:
            cad_modalidade(modalidades)
        elif opcao == 2:
            cad_alunos(alunos)
        elif opcao == 3:
            insere_aluno(alunos_m)
        elif opcao == 4:
            relatorios(relatorio_p)
        elif opcao == 5:
            print("programa finalizado")
        else:
            print("opção invalida")
    menu()
            


              
