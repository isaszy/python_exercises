qntd_alunos = int(input())
nomes = []
notas = []

for _ in range(qntd_alunos):
    nome = input()
    nota = float(input())
    nomes.append(nome)
    notas.append(nota)

#media
soma = 0
for valor in notas:
    soma += valor
media = soma/len(notas)

#verificar se nota maior q media
for posicao, elemento in enumerate(notas):
    if elemento > media: 
        print(nomes[posicao])   #printar o aluno dessa posição
