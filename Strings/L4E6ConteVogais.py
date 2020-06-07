def conte_vogais (string: str) -> int:
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    contador = 0
    for letra in string:
        if letra in vogais:
            contador += 1
    return contador

print(conte_vogais('Erikizinho'))
