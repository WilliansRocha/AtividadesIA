peso = 0
altura = 0
imc = 0
print("[------CALCULADORA IMC------]")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura: "))

imc = (peso / (altura * altura))
imc = round(imc, 2)
if(imc > 0 and imc < 18.5):
    print("Você está abaixo do peso ideal, seu Indice de Massa Corpórea é: ", imc)
elif(imc >= 18.5 and imc < 25):
    print("Você está com peso ideal, seu Indice de Massa Corpórea é: ", imc)
elif(imc >= 25 and imc < 30):
    print("Você está com sobrepeso, seu Indice de Massa Corpórea é: ", imc)
elif(imc >= 30 and imc < 40):
    print("Você está com obesidade, seu Indice de Massa Corpórea é: ", imc)
else:
    print("Você está com obesidade mórbida, seu Indice de Massa Corpórea é: ", imc)
    
        
    
        