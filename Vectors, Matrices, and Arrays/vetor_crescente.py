tamanho = int(input())
v1 = []
for _ in range(tamanho):
    valor = int(input())
    v1.append(valor)
def crescente(vetor):
    for i, n in enumerate(v1):
        if valor < n:
            return 'NAO'
    return 'SIM'
    
print(crescente(v1))
