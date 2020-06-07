def data_extenso (data):
    dia = data[0:2]
    aux_mes = data[3:5]
    aux_ano = data[6:]
    
    meses_nomes  = ['none', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
                    'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                    'Novembro', 'Dezembro']
    
    posicao_mes = int(aux_mes)
    mes = meses_nomes[posicao_mes]
    return f'{dia} de {mes} de {aux_ano}'
    
print(data_extenso('17/03/2001'))
