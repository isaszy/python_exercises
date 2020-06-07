"Lista de String"

def listadeString(frase: str) -> list:
	listaPalavras = []
	palavra = ''
	for letra in frase:
		if letra == " ":
			listaPalavras.append(palavra)
			palavra = ''
		else:
			palavra += letra
	listaPalavras.append(palavra)

	return listaPalavras
