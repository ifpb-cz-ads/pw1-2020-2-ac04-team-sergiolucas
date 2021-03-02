# 18) Escreva um programa que calcule o resto da divisão inteira entre dois números.
# Utilize apenas as operações de soma e subtração para calcular o resultado.


primeiroValor = int(input('Digite o primeiro número: '))
segundoValor = int(input('Digite o segundo número: '))

aux = primeiroValor
resto = primeiroValor
quociente = 0

while aux > 0:
    resto = resto - segundoValor
    aux = aux - segundoValor
    quociente = quociente + 1
if resto != 0:
    print('O quociente da divisão é: ', quociente - 1)
else:
    print('O quociente da divisão é: ', quociente)
if resto < 0:
    print('O resto da divisão é: ', resto + segundoValor)
else:
    print('O resto da divisão é: ', resto)
