from src import bingo

mi_carton = [
        [3,12,6,1040432,0,0,0,3,0],
        [0,0,0,0,0,0,0,0,0],
        [2,16,17,0,0,0,0,0,95]
    ]

cant_celdas_ocupadas = bingo.contar_celdas_ocupadas(mi_carton)

def test_no_menos_de_15():
    assert cant_celdas_ocupadas != 15

def test_no_mas_de_15():
    assert cant_celdas_ocupadas != 15

def test_sin_colums_vacias():
    assert bingo.sin_colums_vacias(mi_carton) == False

def test_sin_filas_vacias():
    assert bingo.sin_filas_vacias(mi_carton) == False

def test_sin_numeros_repeditos():
    assert bingo.sin_numeros_repeditos(mi_carton) == False

def test_mayores_abajo():
    assert bingo.mayores_abajo(mi_carton) == False

def test_celdas_ocupadas_1_a_90():
    assert bingo.celdas_ocupadas_1_a_90(mi_carton) == False

def test_mayores_a_la_derecha():
    assert bingo.mayores_a_la_derecha(mi_carton) == False 

def test_rellenitos():
    assert bingo.completos_segui2(mi_carton) == False

def test_vacio_comotualma():
    assert bingo.vacios_segui2(mi_carton) == False
 