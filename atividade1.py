velocidade = 0
valormulta = 0

velocidade = float(input("Digite a velocidade do carro: "))
if(velocidade > 80):
    valormulta = (velocidade - 80) * 5
    print("Você excedeu a velocidade máxima, sua multa será de: ", valormulta)
else:
    print("Você estava dentro da velocidade permitida ")


    