from src.bingo import carton 

def test_filas_vacias():
	mi_carton=carton()
	i=0
	j=0
	cant1=0
	cant2=0
	for i in range(3):
		cant1=0
		for j in range(9):
			cant1=cant1+mi_carton[i][j]
		if cant1>0:
			cant2+=1
	assert cant2==3
