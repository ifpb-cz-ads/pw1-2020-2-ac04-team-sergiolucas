# 13) Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

loop = True
soma = 0
quantidade = 1
media = 0

while loop:
    numero = int(input('Digite um número inteiro diferente de zero, ou digite zero para encerrar: '))
    if numero != 0:
        soma = soma + numero
        quantidade = quantidade + 1
    else:
        loop = False

print('A quantidade de valores inseridos é de: ', quantidade)
print('A soma dos valores inseridoe é de: ', soma)
print('A média aritmética dos valores inseridos é de: ', soma / quantidade)
