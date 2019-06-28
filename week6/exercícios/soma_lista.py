
#recursivo
def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

#lista = [1,2,3,4,5]
    

#normal
'''def soma_lista_normal(lista):
    somador = 0
    for i in range(len(lista)):
        somador = somador + lista[i]'''
