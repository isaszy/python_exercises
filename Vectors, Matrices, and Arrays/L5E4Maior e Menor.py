"Maior e menor valor de uma lista vetores"

def maiormenor(lista):
	if len(lista) == 0:
		return None
	maior = lista[0]
	for elemento in lista[1:]:
		if elemento > maior:
			maior = elemento
	maiorelemento = maior
	menor = lista[0]

	for elemento in lista[1:]:
		if elemento < menor:
			menor = elemento
	return maior, menor
