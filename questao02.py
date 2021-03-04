#Faça um programa para escrever a contagem regressiva 
#do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

inicio = 10
disparo = -1

while inicio >= disparo:
    if(inicio > disparo):
        print(inicio)
        inicio = inicio -1
    else:
        print("Fogooo!")
        inicio = inicio - 1