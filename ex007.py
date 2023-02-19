n = int(input("Digite o seu contador onde deve ser maior que zero:"))
p = n
soma = 0
while n > 0:
    x = int(input("Digite um número:"))
    soma = soma + x
    n -= 1
media = soma/p
print("SUA MÉDIA É DE",media)
