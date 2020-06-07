n = int(input()) #quantidade de linhas e colunas

def criaMatriz(n): #Criando matriz unitária 
    matriz = []
    for i in range(n):
        matriz.append([0]*n)
    return matriz

def addValores(matriz):
    tamanho = len(matriz)
    for i in range(tamanho): #para cada linha 
        for j in range(tamanho): #em cada coluna
            matriz[i][j] = int(input()) #adiciona valor
    return matriz

def somaAcimaDig(matriz):
    tamanho = len(matriz)
    soma = 0 
    for i in range(tamanho): #exclui a ultima linha
        for j in range(tamanho):
            if j > i:
                soma += matriz[i][j]
    return soma

soma_diag = somaAcimaDig(addValores(criaMatriz(n)))
print(soma_diag)
