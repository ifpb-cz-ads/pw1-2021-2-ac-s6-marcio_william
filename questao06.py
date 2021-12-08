n = int(input("Tabuada de: "))
inicio = int(input("Iniciar do numero: "))
fim = int(input("Terminar no numero: "))

while inicio <= fim:
    resultado = inicio * n
    print(str(inicio) + " x "+ str(n) + " = " + str(resultado))
    inicio=inicio+1