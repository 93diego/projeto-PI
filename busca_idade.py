def buscar_idade(idade):
    idade = 0
    contador = 0
    with open("inscricoes_aluno.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            idade_temp = int(dados[1])
            idade = idade + idade_temp
            contador += 1
        media = idade / contador
        print(f"\n A média de idade entre os alunos é de {media:.2f} anos!")
