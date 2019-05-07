def soma_matrizes(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        lista_somada = [] 
        for i in range(len(m1)):
            linha = []
            lista_somada.append(linha)
            for j in range(len(m1[i])):
                linha.append(m1[i][j] + m2[i][j])
        return lista_somada
    else: 
        return False

'''
matriz1 = [[1, 2, 3], [4, 5, 6]]
matriz2 = [[2, 3, 4], [5, 6, 7]]
soma = soma_matrizes(matriz1, matriz2)
print(soma)
'''


