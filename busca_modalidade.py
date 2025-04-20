def buscar(teste):

    buscar_m = input("digite o que voce quer buscar")

    with open('inscricoes.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip() .split(',')
            if dados[0] == buscar_m:
                print(f" atualmente tem {dados[1]} vagas!")

