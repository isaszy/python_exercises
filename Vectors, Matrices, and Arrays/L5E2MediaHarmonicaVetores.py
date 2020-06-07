"Media harmonica vetores de uma lista"

def media_harmonica_vetores(vetor: list) -> float:
    harm: float = 0
    soma: int = 0
    for elemento in vetor:
        soma += 1/elemento
    harm = 2 / soma
    return harm

print(media_harmonica_vetores([1, 1]))
