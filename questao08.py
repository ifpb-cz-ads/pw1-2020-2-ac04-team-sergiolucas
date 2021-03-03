primeiro = int(input("Informe o primeiro número: "))
segundo = int(input("Informe o segundo número: "))
contador = 0
aux1 = primeiro


while(aux1 >= segundo):
    aux1 = aux1 - segundo
    contador = contador + 1
print("O valor da divisão de %d por %d é: %d e o resto é: %d"%(primeiro, segundo, contador, aux1))


