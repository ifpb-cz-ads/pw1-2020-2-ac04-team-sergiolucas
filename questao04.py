#Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3

cont = 0
fim = 10
x = 1

while cont < fim:
    while x % 3 != 0:
        x = x + 1
    print(x)
    cont = cont + 1
    x = x + 1