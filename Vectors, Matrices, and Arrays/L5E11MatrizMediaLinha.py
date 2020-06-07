"Matrizes Média por linha"

def nLinhas(matriz):
	return len(matriz)

def nColunas(matriz):
	return len(matriz[0])

def lista_media(matriz: list) -> list:
    media_aluno: float = 0
    soma = 0
    medias: list = []
    for i in range(nLinhas(matriz)):
        for j in range(nColunas(matriz)):
            soma += matriz[i][j]
        media_aluno = soma / nColunas(matriz)
        medias.append(media_aluno)
        soma = 0
    return medias

notas = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(lista_media(notas))
