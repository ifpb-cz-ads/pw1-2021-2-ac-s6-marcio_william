total = 0

while True:
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    if codigo ==1:
        total += quantidade *0.5
    elif codigo == 2:
        total += quantidade
    elif codigo ==3:
        total += quantidade * 4
    elif codigo == 5:
        total += quantidade *7
    elif codigo == 9:
        total += quantidade *8
    elif codigo ==0:
        break
    else:
        print("Código inválido")

print(f"Total: {total}")