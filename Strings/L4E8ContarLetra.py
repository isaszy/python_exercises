def contar_letra (string: str, letra: str) -> int:
	cont  = 0
    for letra in string:
        if letra in string:
            cont += 1
    return cont

print(contar_letra('casa', 'a'))
