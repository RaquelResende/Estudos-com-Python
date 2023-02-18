salario = float(input("Digite seu salário aqui:"))
base = 1800

if salario > base:
    salario = salario * 1.13

else:
    salario = salario * 1.10


print("Seu salário calculado é de: R$",salario)