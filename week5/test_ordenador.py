import ordenador
import pytest
from conta_tempos import ContaTempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()
    
    @pytest.fixture
    def l_quase(self):
        c = ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                return False
            else:
                return True

    def teste_bubble_sort_aleatoria(self, o, l_aleatoria):
        o.bubble_sort(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def teste_short_bubble_sort(self, o, l_quase):
        o.short_bubble_sort(l_quase)
        assert self.esta_ordenada(l_quase)

    def teste_selection_sort(self, o, l_aleatoria):
        o.selection_sort(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)