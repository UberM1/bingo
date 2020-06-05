from src import bingo

mi_carton = bingo.Generar()

def test_mayores_abajo():
    assert bingo.mayores_abajo(mi_carton)
