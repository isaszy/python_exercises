def palindrome (palavra: str) -> bool:
    listaLetra = []
    for letra in palavra:
        listaLetra.append(letra)
    if listaLetra[0:] == listaLetra[::-1]:
        return True
    return False
        
        
print(palindrome('casa'))
