L = int(input()) #quantidade de alunos linhas
C = int(input()) #quantidade de notas colunas

def criaMatriz(valor, linhas, colunas): #Criando matriz unitária 
	matriz = []
	for i in range(linhas):
		matriz.append([valor]*colunas)
	return matriz

def addNotas(matriz, linhas, colunas):
    for i in range(linhas): #para cada linha 
        for j in range(colunas): #em cada coluna
            matriz[i][j] = float(input()) #adiciona a nota do aluno
    return matriz

def calculaMedia(matriz, linhas, colunas):
    cont, media = 0, 0 #armazenar a soma das notas e para calcular a media
    for i in range(linhas):
        for j in range(colunas):
            cont += matriz[i][j]
            media = cont / colunas
        matriz[i][j+1] = media #quando sair do laço adiciona na
        #4 coluna a media do aluno
        cont = 0
    return matriz
        
mtxNotasMedia = calculaMedia(addNotas(criaMatriz(0, L, C+1), L, C), L, C)

print(mtxNotasMedia)
    
