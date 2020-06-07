n: int = int(input()) #quantidade de elementos no vetor

def cria_vetor(n: int) -> list: #função que cria vetor com n elementos
    vetor: list = []  #vetor vazio
    for _ in range(n): #percorrendo por n vezes
        novo_valor: int = int(input()) #entrada do elemento
        vetor.append(novo_valor) #adicionando elementos ao vetor
    return vetor

def espelho(vetor: list) -> str: #função que verifica se o vetor é um espelho
    tamanho = len(vetor) #tamanho do vetor/quantidade de elementos
    metade = tamanho // 2
    
    if tamanho % 2 != 0:  #para vetor ímpares
        if vetor[:metade] == vetor[:metade:-1]:
            return 'SIM'
        return 'NAO'
    
    if vetor[:metade] == vetor[:metade-1:-1]: #vetores pares
        return 'SIM'
    return 'NAO'

print(espelho(cria_vetor(n)))
