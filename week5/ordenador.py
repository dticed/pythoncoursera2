class Ordenador:

    def selection_sort(self, lista):
        fim = len(lista)
        for i in range(fim-1):
            posicao_do_minimo = i
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            lista[posicao_do_minimo], lista[i] = lista[i], lista[posicao_do_minimo]


    def bubble_sort(self,lista):
        fim = len(lista)
        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def short_bubble_sort(self, lista):
        fim = len(lista)
        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return 
