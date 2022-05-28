votar = 0
datanasc = 0
dataatual = 2022
datanasc = float(input("Digite o ano de nascimento: "))

votar = dataatual - datanasc
if(votar >= 18):
    print("Você pode votar ")
else:
     print("Você ainda não tem idade suficiente para votar ")
     