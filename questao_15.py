# Escreva um programa que exiba uma lista de opções (menu): adição, subtração,
# divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a
# opção "saída" seja escolhida.

print('1- Adição')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')
print('5- Sair')
opcao = input('Escolha uma opção, ou digite 5 para sair: ')

while opcao != '5':
    tabuada = int(input('Digite um número para exibir a tabuada: '))
    if opcao == '1':
        i = 1
        while i <= 10:
            n = tabuada + i
            print('{0:2d} + {1:2d} = {2:3d}'.format(tabuada, i, n))
            i = i + 1
    elif opcao == '2':
        i = 1
        while i <= 10:
            n = tabuada - i
            print('{0:2d} - {1:2d} = {2:3d}'.format(tabuada, i, n))
            i = i + 1
    elif opcao == '3':
        i = 1
        while i <= 10:
            n = tabuada * i
            print('{0:2d} x {1:2d} = {2:3d}'.format(tabuada, i, n))
            i = i + 1
    elif opcao == '4':
        i = 1
        while i <= 10:
            n = tabuada / i
            print('{0:2d} / {1:2d} = {2:3f}'.format(tabuada, i, n))
            i = i + 1
    else:
        print('Por favor, escolha uma opção válida!')

    print('1- Adição')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print('5- Sair')
    opcao = input('Escolha uma opção, ou digite 5 para sair:')
