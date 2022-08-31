#Ecercicios 05 - PYTHON - ANTECESSOR E SUCESSOR
#N=int(input('Digite um número: '))
#print (f'Analisando o numero {N} seu antecessor é {N-1} e seu sucessor é {N+1}')

#Ecercicios 06 - PYTHON - RAIZ QUADRADA
#n=int(input('Digite um número: '))
#print(f'O dobro de {n} é igual há {n*2}')
#print(f'O triplo de {n:.2f} é igual há {n*3}')
#print(f'A raiz quadrada de {n:.2f} é igual há {pow(n, (1/2))}')

#Ecercicios 07 - PYTHON - MEDIA
#n1=float(input('Sua primeira nota foi: '))
#n2=float(input('Sua segunda nota foi: '))
#print (f'Com as notas {n1:.1f} e {n2:.2f} sua média foi de {(n1+n2)/2:.2f}')

#Ecercicios 08 - PYTHON - METROS, CENTIMETROS, MILIMETROS...
#V=float(input('Digite em metros a medida que gostaria de converte: ' ))
#M=input('Agora escolha uma das medias ' 'CENTIMETROS:' 'MILIMETROS OU ' 'KILOMETROS: ').upper()
#if M == 'CENTIMETROS':
#    (print (f'O valor em centimentros é {V*100:.2f}cm'))
#elif M == 'MILIMETROS':
 #   (print(f'O valor em milimetros é {V*1000:.2f}mm'))
#elif M == 'KILOMETROS':
 #   (print(f'O valor em kilometros é {V/1000:.2f}km'))

#1Ecercicios 09 - PYTHON - TABOA
#n=int(input('Digite um numero para saber sua tabuada: '))
#print (f'{n} * {1:2} = {(n*1)}')
#print (f'{n} * {2:2} = {(n*2)}')
#print (f'{n} * {3:2} = {(n*3)}')
#print (f'{n} * {4:2} = {(n*4)}')
#print (f'{n} * {5:2} = {(n*5)}')
#print (f'{n} * {6:2} = {(n*6)}')
#print (f'{n} * {7:2} = {(n*7)}')
#print (f'{n} * {8:2} = {(n*8)}')
#print (f'{n} * {9:2} = {(n*9)}')
#print (f'{n} * {10:2} = {(n*10)}')

#Ecercicios 10 - PYTHON -  DOLAR PARA REAL
#import time
#print('Olá vou te ajudar á cambiar o seu dinheiro para o dolar ')
#time.sleep(2)
#v=float(input('Para que eu possa te ajudar me diga o valor que deseja cambiar : R$ '))
#print(f'O valor escolhido cambiado para o dolar é equivalente á US${v/4.96:.2f}')

#Ecercicios 11 - PYTHON - CALCULANDO Á AREA
#a=float(input("Olá vamos calcular a area da sua parede, primeiro me diga o valor de sua altura: "))
#l=float(input('Agora me dia o valor de sua largura para sabermos a area: '))
#area=a*l
#v=area/7.5
#ml=v*1000
#print(f'Sendo a altura {a} e a largura {l}, há area de sua parede é de {area:.2f}m²')
#if area >= (7.5):
#    print(f'Sendo que cada litro de tinta pinta 7.5m² você precisará de {area/7.5:.2f}l para pintar sua parede:')
#else:
#    print(f'Sendo que cada litro de tinta pinta 7.5m² você precisará de {ml:.2f}ml')

#Ecercicios 12 - PYTHON - PREÇO DE UM PRODUTO COM DESCONTO
#import time
#print('Olá tudo bem? \nEstamos hoje em um ótimo dia, por isso lhe daremos 5% de desconto em qualquer um dos 3 produtos abaixo: ')
#time.sleep(5)
#P = input('Joystick\n' 'Kayboard\n' 'ou Mouse \nQual deseja? ').upper()
#J=float(237.88)
#K=float(345.77)
#M=float(100.00)
#D=float(0.05)
#JD=float(J*0.05)
#KD=float(K*0.05)
#MD=float(M*0.05)
#if P[0] == 'J':
#    print(f'O valor total do Joystick é de R${J:.2f}')
#    print(f'Com os 5% de deconto fica um valor final de R${J-JD:.2f}')
#elif P[0] == 'K':
#    print(f'O valor total do Keyboard é de R${K:.2f}')
#    print(f'Com os 5% de desconto fica um valor final de R${K-KD:.2f}')
#elif P[0] == 'M':
#    print(f'O valor total do Mouse é de R${M:.2f}')
#    print(f'Com os 5% de desconto fica um valor final de R${M-MD:.2f}')
#else:
#    print('Sinto muito, más no momento só temos esses produtos a venda.')
#print ('''Colocando
#os 3 pontinho de cima
#posso descer quantas linhas quiser!''')

#Ecercicios 13 - PYTHON - REAJUSTE SALÁRIAL
#S = float(input('Olá, vou te judar a calcular o seu reajuste sálarial\nme diga qual o valor do seu salario: '))
#P = float(input('Agora me diga qual foi o valor do seu reajuste sem simbolos e no lugar de vírgula use pontos ok!: '))
#R=(S*(P/100))
#RS=S+R

#Ecercicios 14 - PYTHON - GRAUS CELCIUS E FAHRENHEIT
#C = float(input('Olá, me informe a temperatura em graus Cº que deseja transforma em graus Fº: '))
#F = ((9*C)/5)+32
#print (f'{C}Cº equivalem a graus {F}Fº ')
#import time
#import math
#from math import trunc

#Ecercicios 15 - ALUGUEL DE UM CARRO
#time.sleep(4)
#print('Olá nossos carros tem uma diaria de 60R$ e um valor de 0,15R$ por KM rodado.')
#time.sleep(6)
#print('Caso deseje alugar por frações de tempo saiba que cobramos 2R$ por minutos e 10R$ por hora.')
#time.sleep(5)
#tempo = input('Sabendo disso me diga gostaria de alugar o carro por minutos, horas ou dias? ').upper()
#if tempo == 'HORAS':
#    H=float(input('Por quantas horas gostaria de alugar? '))
#    if H <= 23 :
#        print(f'Nesse caso você pagará {H*10}, isso sem contar os KM rodados que serão verificados e calculado na entrega do veiculo OK!')
#    elif H > 23 :
#        print(f'Nesse caso você pagará {H*2.5}, isso sem contar os KM rodados que serão verificados e calculados na entrega do veiculo OK!')
#elif tempo == 'MINUTOS':
#    M=float(input('Por quantos minutos gostaria de alugar? '))
#    if M <= 59 :
#        print(f'Nesse caso você pagará {M*2}, isso sem contar os KM rodados que serão verificados e calculados na entrega do veiculo OK!')
#    elif M > 59 :
#        print(f'Nesse caso você pagará {math.ceil(M * 0.166):.2f}, isso sem contar os KM rodados que serão verificados e calculados na entrega do veiculo OK!')
#elif tempo == 'DIAS':
#    D=float(input('Por quantos dias gostaria de alugar? '))
#    if D <= 31:
#        print(f'Nesse caso você pagará {D*60}, isso sem contar os KM rodados que serão verificados e calculados na entrega do veiculo OK!')
#    if D > 31 :
#        print('Desculpe só podemos calcular um periodo maximo de 30 dias ok')
#else :
#    print('Desculpe acredito que deva ter digitado errado verifique novamente sua resposta okay!')


#Ecercicios 16 - QUEBRANDO UM NÚMERO EM PORÇÃO INTEIRA
#from math import trunc
#import math
#print('Me diga qualquer número e vou le dizer sua porção interia :')
#N = float(input('Número : '))
#print (f'Sua porção inteira é {math.trunc(N)}')

#Ecercicios 17 - CATETO OPOSTO, HIPOTENUSA E CATETO ADJACENTE
#co = float(input('Qual o cateto oposto ? '))
#ca = float(input('Qual o cateto adjacente ? '))
#HI = (co**2+ca**2)**(1/2)
#print (f'A hipotenusa equivale a {HI:.2f} ')







