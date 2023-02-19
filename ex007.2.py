a = 10
b = 20
par = 0
impar = 0

while a <= b:
    if a % 2 == 0:
        par += 1
    else:
        impar += 1
    a +=1
print("A QUANTIDADE DE PAR SÃO {} \n A QUANTIDADE DE IMPARES SÃO: {}".format(par,impar))