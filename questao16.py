numero = int(input("Digite o número: "))

for i in range(2,numero):
    if (numero%i==0):
        print(f"{numero} não é primo")
        break
    else:
        print(f"{numero} é primo")
        break
