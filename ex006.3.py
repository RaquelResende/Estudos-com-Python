print("Didite uma lentra dentro das opções abaixo")
print(" C é igual a casa; \n I igual a indústria;  \n E igual a empresa.")

tipo = input("Digite aqui o tipo:")

if tipo == "C" or tipo == "c":
     kwh = float(input("Digite o seu consumo em kwh:"))
     if kwh <= 600:
         preco = kwh*0.45
     else:
         preco = kwh*0.65

elif tipo == "I" or tipo == "i":
   tipo = "industria"
   kwh = float(input("Digite o seu consumo em kwh:"))
   if kwh <= 1200:
       preco = kwh * 0.75
   else:
       preco = kwh * 0.95

elif tipo == "C" or "c":
    tipo = "empresa"
    kwh = float(input("Digite o seu consumo em kwh:"))
    if kwh <= 6000:
        preco = kwh * 0.70
    else:
        preco = kwh * 0.80

else:
    print("Digite a letra conforme na legenda!")

print("O tipo {} consume em kwh por mês R${}".format(tipo,preco))



