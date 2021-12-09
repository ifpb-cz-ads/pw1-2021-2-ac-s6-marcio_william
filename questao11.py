depositoInicial = int(input("Deposito inicial: "))
depositoMensal = float(input("Deposito mensal: "))
taxaDeJuros = float(input("Taxa de porcentagem Juros: ")) / 100
mes = 1
lucro = 0
saldo = depositoInicial

while mes <= 12:
    saldo = saldo + taxaDeJuros * saldo
    print(str(mes) + " mês = " + str(round(saldo, 2)))
    saldo += depositoMensal
    mes=mes+1

totalGanho = saldo - depositoInicial - depositoMensal*11
print("O total ganho foi " + str(round(totalGanho, 2)))