depósito = float(input("informe o depósito inicial: "))
juros = float(input("Informe a taxa de juros (Sem o %): "))
depósito_mês = float(input("informe o depósito mensal: "))
mês = 1
periodo = 12
saldo = depósito


while mês <= periodo:
    saldo = saldo + (saldo * (juros / 100)) + depósito_mês
    print("Saldo do mês %d é de R$ %.2f."%(mês, saldo))
    mês = mês + 1

print("O ganho obtido com os juros foi de R$ %.2f."%(saldo-depósito))