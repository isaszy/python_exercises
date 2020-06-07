" Média vetores de uma lista"

def media_vetores(vetor: list) -> float:
    soma: int = 0
    media: float = 0
    tamanho: int = len(vetor)
    for elemento in vetor:
        soma += elemento
    media = soma / tamanho
    return media

v1 = [1, 2, 3]
print(media_vetores(v1))
