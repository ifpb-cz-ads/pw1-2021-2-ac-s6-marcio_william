numeroFinal = int(input("Digite o número final: "))

for num in range(1,numeroFinal):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(f"{num}")
            break