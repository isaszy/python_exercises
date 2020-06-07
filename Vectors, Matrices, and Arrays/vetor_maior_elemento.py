numero_elementos = int(input())

def formar_lista(numero_elementos: int) -> list:
    lista: list = []
    for posicao in range(numero_elementos):
        elemento: int = int(input())
        lista.append(elemento)
        
    return lista
    
def maior(lista):
	maior: int = lista[0]
	for elemento in lista[1:]:
		if elemento > maior:
			maior = elemento
	return maior
	
print(maior(formar_lista(numero_elementos)))
