nome = ""
anosemprego = 0
salario = 0
novosalario = 0

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
anosemprego = float(input("Digite o numero de anos que você trabalha na empresa: "))
if(anosemprego > 0 and anosemprego <= 3):
    novosalario = (salario + ((salario /100) * 3))
    print("Senhor(a)", nome, " seu salario reajustado será de R$", novosalario)
elif(anosemprego > 3 and anosemprego < 10):
    novosalario = (salario + ((salario /100) * 12.5))
    print("Senhor(a)", nome, " seu salario reajustado será de R$", novosalario)
else:
    novosalario = (salario + ((salario /100) * 20))
    print("Senhor(a)", nome, " seu salario reajustado será de R$", novosalario)  
    
