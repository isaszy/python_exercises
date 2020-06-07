n = int(input()) #quantidade de linhas e colunas

def cria_matriz(n: int): #matriz quadrada
	matriz: list = []
	for i in range(n):
		matriz.append([0]*n)
	return matriz

def sequencia_diagonal(matriz: list):
    tamanho: int = len(matriz)
    valor = 1
    for i in range(tamanho): #para cada linha
        for j in range(tamanho): #em cada coluna
            matriz[i][j] = valor
            valor += 1
        valor = matriz[i][1]
    return matriz
            
print(sequencia_diagonal(cria_matriz(n)))
