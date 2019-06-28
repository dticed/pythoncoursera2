import random
import ordenador
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = ordenador.Ordenador()

        print("Comparando com listas aleatórias.")
        antes = time.time()
        o.bubble_sort(lista1)
        depois = time.time()
        print("BubbleSort demorou: ", depois - antes)

        antes = time.time()
        o.selection_sort(lista2)
        depois = time.time()
        print("SelectionSort demorou: ", depois - antes)

        print("\nComparando com listas quase ordenadas.")

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        antes = time.time()
        o.short_bubble_sort(lista1)
        depois = time.time()
        print("BubbleSort demorou: ", depois - antes)

        antes = time.time()
        o.selection_sort(lista2)
        depois = time.time()
        print("SelectionSort demorou: ", depois - antes)

    

c = ContaTempos()

c.compara(1000)
