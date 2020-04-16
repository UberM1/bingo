from src.bingo import carton

def test_columnas_vacias():
	mi_carton=carton()
	i=0
	cant=0
	for i in range(9):
		if mi_carton[0][i]+mi_carton[1][i]+mi_carton[2][i]>0:
			cant=cant+1
	assert cant==9
		
		
