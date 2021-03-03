# Modifique o programa anterior de forma 
# que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10

n = int(input("Tabuada de: "))
inicio = int(input("Informe em qual número começar: "))
fim = int(input("Informe em qual número parar: "))

if(inicio < fim):
    while inicio <= fim:
	    print("%d x %d é: %d"%(n,inicio,n * inicio))
	    inicio = inicio + 1
else:
    print("Informe um intervalo válido!")