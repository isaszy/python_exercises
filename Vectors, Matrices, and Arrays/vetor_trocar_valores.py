v1 = []
v2 = []

tamanho = int(input())

for i in range(tamanho): #vetor 1
    positivo = int(input())
    v1.append(positivo)
v2 = v1

i = int(input())
j = int(input())

if i > tamanho-1 or j > tamanho-1:
    print(v1)
else:
    valor_i = v1[i]
    valor_j = v1[j]
    v2[i] = valor_j
    v2[j] = valor_i

print(v2)
