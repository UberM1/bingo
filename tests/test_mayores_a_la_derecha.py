from src import bingo

mi_carton = bingo.Generar()

def test_mayores_a_la_derecha():
    assert bingo.mayores_a_la_derecha(mi_carton)
