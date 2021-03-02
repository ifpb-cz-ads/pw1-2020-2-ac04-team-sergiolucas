# 7) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do
# primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o
# resultado. Lembre-se de que podemos entender a multiplicação de dois números como
# somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

num1 = int(input("Digite o número Multiplicandor: "))
num2 = int(input("Digite o número que será Multiplicado: "))

soma = 0
multiplicador = 0
multiplicando = 0

if num1 < num2:
    multiplicador = num1
    multiplicando = num2
else:
    multiplicador = num2
    multiplicando = num1

x = 0
while x != multiplicador:
    soma = soma + multiplicando
    x = x + 1
print(f'Resultado = {soma}')
