from src.bingo import carton
def test_contar_celdas_ocupadas():
	car = carton()
	i=0
	j=0
	k=0
	l=0
	for j in range(9)
		for i in range(3)
			for k in range(j,9)
				for l in range(i,3)
					if car[i][j]!= 0 && car[k][l]!=0:
						assert car[i][j]!=car[k][l]
