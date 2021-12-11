depositoInicial = int(input("Deposito inicial: "))
taxaDeJuros = float(input("Taxa de porcentagem Juros: ")) / 100
mes = 1
lucro = 0
saldo = depositoInicial

while mes <= 12:
    saldo = saldo + taxaDeJuros * saldo
    print(str(mes) + " mês = " + str(round(saldo, 2)))
    mes=mes+1

totalGanho = saldo - depositoInicial
print("O total ganho foi " + str(round(totalGanho, 2)))