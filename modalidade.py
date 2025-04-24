from voltar_menu import menu_prin

modalidade = []
menu_1 = []


def cad_modalidade(modalidades):
    nome = input("modalidade: ")
    vagas = int(input("vagas: "))
    modalidade.append({"nome": nome, "vagas": vagas})
    print(f"modalidade '{nome}' criada com {vagas} vagas")
    menu_prin(menu_1)


##    cad_modalidade()
##    print(modalidade)
##    for i in range(len(modalidade)):
##        print(i)
##    for g in modalidade:
##        print((g["nome"]))
