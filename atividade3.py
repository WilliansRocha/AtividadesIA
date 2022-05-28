distancia = 0
preco = 0
distancia = float(input("Digite a distância que deseja percorrer em km: ")) 
if(distancia <= 200):
    preco = distancia * 0.50
    print("O valor da passagem será: ", preco)
else:
     preco = distancia * 0.45
     print("O valor da passagem será: ", preco)
