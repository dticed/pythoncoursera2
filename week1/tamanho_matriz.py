def dimensoes(matriz):
    if len(matriz) == 0:
        print("0X0")
    else:
        linha = len(matriz)
        coluna = len(matriz[0])
        print(str(linha) + "X" + str(coluna))
    