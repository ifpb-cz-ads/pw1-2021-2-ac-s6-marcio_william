soma =0
contador =0
while True:
    numero = int(input("Digite o número: "))
    if(numero ==0):
        break
    soma += numero
    contador +=1
print(f"Soma: {soma}")
print(f"Media: {soma/contador}")