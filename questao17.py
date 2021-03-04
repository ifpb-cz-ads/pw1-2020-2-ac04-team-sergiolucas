numero = int(input('Digite um número inteiro positivo: '))
contador = 0
num = 2

while contador < numero:
    primo = True
    for i in range(2, num):
        if num % i == 0:
           primo = False
           break
    if primo == True:
        print(num)
        contador += 1
    num += 1