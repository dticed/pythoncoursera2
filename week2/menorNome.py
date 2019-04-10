def menor_nome(nomes):
    lista = nomes[0].strip()
    menor = len(nomes[0].strip())
    for i in nomes:
        i = i.strip()
        if len(i) < menor:
            menor = len(i)
            lista = i
    return lista.capitalize()

'''print(menor_nome(['maria   ', 'josé', 'PAULO', 'Catarina']))
print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill', 'iu']))
print(menor_nome(['LU ', ' josé ', 'PAULO', 'Catarina']))
print(menor_nome(['zé', ' lu', 'fê']))'''