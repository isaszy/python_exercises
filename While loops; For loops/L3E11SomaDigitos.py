def ultimoDigito (n: int) -> int:
    return n % 10

def removeDigito (n: int) -> int:
    return n // 10

def somatoria_digitos(n: int) -> int:
    soma = 0
    while n > 0:
        soma += ultimoDigito(n)
        n = removeDigito(n)
    return soma

n = int(input())
print(somatoria_digitos(n))