import pytest
import Triangulo

#Exemplo de teste 1(simples sem criar classes)
'''def testa_perimetro():
        t = Triangulo.Triangulo(1,1,1)
        assert t.perimetro() == 3'''

#Exemplo de teste 3
'''@pytest.mark.parametrize("entrada, esperado", [
    ((1,1,1),(3)),
    (),
    (),
    ()
    ])'''

'''def testa_perimetro(entrada, esperado):
t = Triangulo.Triangulo(entrada)
assert t.perimetro == esperado'''
    

class TestaTriangulo:
    
    
    #Exemplo de teste 2
    '''@pytest.fixture
    def t(self):
        return Triangulo.Triangulo(1,1,1)

    def testa_perimetro(self, t):
        assert t.perimetro() == 3'''

    