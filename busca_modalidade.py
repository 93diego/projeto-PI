def buscar_modalidade(modalidade):

    buscar_m = input("Digite o que voce quer buscar: ")

    with open("inscricoes_aluno.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if dados[2] == buscar_m:
                print(f"\n {dados[0]} está cadastrado em {dados[2]} ")
