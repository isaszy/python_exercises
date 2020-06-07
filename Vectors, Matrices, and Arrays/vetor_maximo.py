v1 = [] #positivo
v2 = [0] #negativo
lista = []

posicoes = int(input())

for i in range(posicoes): #vetor 1
    positivo = int(input())
    v1.append(positivo)
tamanho = len(v1)

i = 1
while i != tamanho-1:
    lista = [v1[i], v1[i-1], v1[i+1]]
    maximo = max(lista)
    v2.append(maximo)
    i += 1
v2.append(0)
print(v2)
