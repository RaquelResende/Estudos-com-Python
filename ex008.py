
for i in range(3):
    nome = input("Digite o nome do aluno:")
    p1 = float(input("Digite a nota do aluno:"))
    p2 = float(input("Digite a segunda nota do aluno:"))
    media = p1 + p2/2
    if media <= 6:
        condicao = "Reprovado!"
    else:
        condicao = "APROVADO"
    print(f"O aluno {nome} atingiu a média {media} e seu estado é {condicao}")
    print("")