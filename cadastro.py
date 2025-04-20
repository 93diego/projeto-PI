def geral(teste):
    
    def cadastrar_inscricao(nome_modalidade, vagas):
        with open('inscricoes.txt', 'a') as arquivo:
            linha = f"{nome_modalidade},{vagas}\n"
            arquivo.write(linha)
        print("Inscrição cadastrada com sucesso!")

    def listar_inscricoes():
        with open('inscricoes.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                print(f"Modalidade: {dados[0]} | Vagas: {dados[1]}")

    nome_modalidade = input("digite a modalidade")
    vagas = int(input("digite as vagas: "))
    cadastrar_inscricao(nome_modalidade,vagas)



    

