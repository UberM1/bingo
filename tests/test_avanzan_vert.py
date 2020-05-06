from src.bingo import carton

def test_contar_celdas_ocupadas():
	car = carton()
	i=0
	j=0
	aux=0
	for j in range(9):
		for i in range(2):	
			aux=car[i][j]
			assert aux<car[i+1][j]
