fim = int(input("Digite o último número a imprimir:"))
x = 1
while x <= fim:
    resto = x % 2
    if x < fim:
        if resto != 0:
            print(x)
    x=x+1