def diminuir(modalidade):
    nova_linha = []
    with open('inscricoes.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(',')
            if dados[0] == modalidade:
                vagas = int(dados[1])
                if vagas > 0:
                    vagas -= 1
                # Atualiza a linha com o novo número de vagas
                linha = f"{dados[0]},{vagas}\n"
            nova_linha.append(linha)

    with open('inscricoes.txt', 'w') as arquivo:
        arquivo.writelines(nova_linha)

modalidade = input("Digite a modalidade: ")
diminuir(modalidade)
