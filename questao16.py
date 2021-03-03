numero = int(input("informe um numero inteiro: "))
divisor = 0 

if numero != 0 and numero != 1: 
    for c in range(1 , numero +1):
        if numero % c == 0: 
            divisor += 1

if divisor == 2:
    print("Numero primo")
else:
    print("Numero nao primo")