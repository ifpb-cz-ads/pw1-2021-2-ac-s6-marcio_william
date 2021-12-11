numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
contador = 1
resultado = 0
resto = 0
while contador <= numero2:
    divisao = numero1 - numero2
    if divisao >= 0:
        numero1 = numero1 - numero2
        resultado = resultado+1
    else:
        resto = numero1
    contador=contador+1

print("Resultado: " + str(resultado))
print("Resto: " + str(resto))