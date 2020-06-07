v1 = []
v2 = []
zero, um, dois, tres, quatro, cinco, seis, sete, oito, nove = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

tamanho = int(input())

for i in range(tamanho): #vetor 1
    positivo = int(input())
    if 0 <= positivo <= 9:
        v1.append(positivo)
    else:
        positivo = int(input())

for elemento in v1:
    if elemento == 0:
        zero += 1
    elif elemento == 1:
        um += 1
    elif elemento == 2:
        dois += 1
    elif elemento == 3:
        tres += 1
    elif elemento == 4:
        quatro += 1
    elif elemento == 5:
        cinco += 1
    elif elemento == 6:
        seis += 1
    elif elemento == 7:
        sete += 1
    elif elemento == 8:
        oito += 1
    else:
        nove += 1
nova_lista = [zero, um, dois, tres, quatro, cinco, seis, sete, oito, nove]
print(nova_lista)
