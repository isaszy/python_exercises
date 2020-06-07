def criaMatriz(valor, m, n): #m linhas n coluna
	matriz = []
	for i in range(m):
		matriz.append([valor]*n)
	return matriz
	
def addValores(matriz, linhas, colunas):
    for i in range(linhas): #para cada linha 
        for j in range(colunas): #em cada coluna
            matriz[i][j] = int(input()) #adiciona a nota do aluno
    return matriz
	
def somaDiagonal(mtx):
	soma = 0
	for i in range(n):
		soma += mtx[i][i]
	return soma

n = int(input())

soma_diagonal = somaDiagonal(addValores(criaMatriz(0, n, n), n, n))

print(soma_diagonal)
