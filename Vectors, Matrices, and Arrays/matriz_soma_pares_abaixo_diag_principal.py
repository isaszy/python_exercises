n: int = int(input())                               #quantidade de linhas e colunas

def cria_matriz(n: int) -> list:                    #Criando matriz unitária 
    matriz: list = []
    for _ in range(n):
        matriz.append([0]*n)
    return matriz

def add_valores(matriz: list) -> list:
    tamanho: int = len(matriz)
    for linha in range(tamanho):                    #para cada linha 
        for coluna in range(tamanho):               #em cada coluna
            matriz[linha][coluna] = int(input())    #adiciona valor
    return matriz

def soma_acima_diagonal(matriz: list) -> int:
    tamanho: int = len(matriz)
    soma: int = 0 
    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] % 2 == 0 and i > j:
                soma += matriz[i][j]
    return soma

soma_diag = soma_acima_diagonal(add_valores(cria_matriz(n)))
print(soma_diag)
