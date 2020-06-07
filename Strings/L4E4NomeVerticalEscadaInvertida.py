def nome_vertical_escada_invertida (nome: str) -> str:
    linha = []
    linha += nome
    print(nome)
    for i in nome:
        linha.pop()
        string = ''.join(linha)
        print(string)
    return ''


print(nome_vertical_escada_invertida('**********************'))
