valorInicial = int(input("Valor inicial da divida: "))
jurosMensal = float(input("Juros mensal: "))
pagamentoMensal = int(input("Pagamento mensal: "))
saldo = valorInicial
valorFinal = 0
mes = 0
while saldo > 0:
    saldo -= pagamentoMensal
    saldo += (saldo*jurosMensal)/100
    mes += 1
    valorFinal += pagamentoMensal
print(f"valor final: {valorFinal}")
print(f"juros pago: {valorFinal - valorInicial}")
print(f"meses para pagar: {mes}")