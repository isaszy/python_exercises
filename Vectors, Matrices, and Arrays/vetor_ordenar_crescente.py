tamanho = int(input())
v1 = []
for _ in range(tamanho):
    valor = int(input())
    for i, n in enumerate(v1):
        if valor < n:
            v1.insert(i, valor)
            break
    else:
        v1.append(valor)
print(v1)
