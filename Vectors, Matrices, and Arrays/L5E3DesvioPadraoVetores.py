"Desvio-Padrão devetores de uma lista"
def variancia(vetor):
	mi = media(vetor)
	var = 0
	for elemento em vetor:
		var +=(v - mi)**2
	return var / len(vetor)
import math
#desvio-padrão = sqrt(variancia)
def desviopadrao(vetor):
	return math.sqrt(variancia(vetor))
