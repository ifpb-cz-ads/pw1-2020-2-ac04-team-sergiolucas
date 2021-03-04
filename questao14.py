print("Caixa Registradora")
total = 0
produto = int(input("\nInforme o codigo do produto ou 0 para encerrar \nprodutos disponíveis 1 - 2 - 3 - 5 - 9: "))

if(produto != 0):
    while produto != 0:
        if(produto == 1):
            total = total + 0.50
        elif(produto == 2):
            total = total + 1.00
        elif(produto == 3):
            total = total + 4.00
        elif(produto == 5):
            total = total + 7.00
        elif(produto == 9):
            total = total + 8.00
        else:
            print("Informe um código válido!\n")
        produto = int(input("\nInforme o codigo do produto ou 0 para encerrar \nprodutos disponíveis 1 - 2 - 3 - 5 - 9: "))
    print("\nOperação Encerrada! O valor total da compra foi R$%.2f"%(total))
else:
    print("Operação finalizada no início, reinicie a máquina!")