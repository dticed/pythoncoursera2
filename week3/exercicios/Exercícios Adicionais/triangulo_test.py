import pytest
import Triangulo

def testa_perimetro():
    t = Triangulo.Triangulo(1,1,1)
    assert t.perimetro() == 3 
    
    t = Triangulo.Triangulo(2,2,2)
    assert t.perimetro() == 6

    t = Triangulo.Triangulo(3,3,3)
    assert t.perimetro() == 9

    t = Triangulo.Triangulo(0,0,0)
    assert t.perimetro() == 0

    t = Triangulo.Triangulo(100,100,100)
    assert t.perimetro() == 300

def testa_tipo_lado():
    t = Triangulo.Triangulo(1,1,1)
    assert t.tipo_lado() == "equilátero"

    t = Triangulo.Triangulo(1,2,2)
    assert t.tipo_lado() == "isósceles"

    t = Triangulo.Triangulo(1,2,3)
    assert t.tipo_lado() == "escaleno"

    t = Triangulo.Triangulo(1,2,1)
    assert t.tipo_lado() == "isósceles"

    t = Triangulo.Triangulo(1,1,2)
    assert t.tipo_lado() == "isósceles"

def testa_triangulo_retangulo():
    t = Triangulo.Triangulo(4,3,5)
    assert t.retangulo() == True

    t = Triangulo.Triangulo(1,1,3)
    assert t.retangulo() == False

    t = Triangulo.Triangulo(12,9,15)
    assert t.retangulo() == True

def testa_semelhantes():
    t = Triangulo.Triangulo()



    
