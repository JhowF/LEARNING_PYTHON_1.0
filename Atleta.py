from datetime import date
hoje = date.today().year
ano =  int(input("Ano de nascimento: "))
print(hoje)
idade = (hoje-ano)
print(f"O atleta tem \033[4;34m{idade}\033[m anos.")

if idade <= 9 :
    print("Classificação: MIRIM")
elif  idade >= 10 and idade <=14 :
    print("Classificação: INFANTIL")
elif idade >= 15 and idade <=19 :
    print("Classificação: JÚNIOR")
elif idade >= 20 and idade <=25 :
    print("Classificação: SENIOR")
elif idade >= 25 and idade <= 35:
    print("Classificação: MASTER ")
elif idade > 35:
    print("Desculpe mas você ultrapassou nossa idade limite")

