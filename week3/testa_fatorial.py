import pytest
import fatorial

@pytest.mark.parametrize("entrada, esperado", [
    (0,1),
    (1,1),
    (-10,0),
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial.fatorial(entrada) == esperado