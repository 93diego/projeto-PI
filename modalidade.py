modalidade = []
while True:
    def cad_modalidade ():
        nome = input("modalidade: ")
        vagas = int(input("vagas: "))
        modalidade.append({"nome": nome,"vagas": vagas})
        #menu_prin()
    cad_modalidade()
    print(modalidade)
    for i in range(len(modalidade)):
        print(i)
    for g in modalidade:
        print((g["nome"]))

