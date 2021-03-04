dívida = float(input("Informe a dívida: "))
juros = float(input("Informe os juros aplicados(Sem o %): "))
pagamento = float(input("Informe o pagamento mensal:"))
mês = 1

if (dívida * (juros/100) >= pagamento):
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = dívida
    juros_pago = 0

    while saldo > pagamento:
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print ("Saldo da dívida no mês %d é de R$ %.2f." %(mês, saldo))
        mês = mês + 1
    
    print ("Para sua dívida de R$%.2f, a %.2f %% de juros," %(dívida, juros))
    print ("você precisará de %d meses, pagando juros de R$%.2f reais." %(mês-1, juros_pago))
    print ("No último mês, você teria um saldo residual de R$%.2f a pagar." %(saldo))