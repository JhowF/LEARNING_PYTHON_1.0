print('Olá te ajudo a resolver qualquer exercicio de ltpotência, muiplicação, divisão, adição e/ou subtração.', end=' ')
print('Vamos comerçar OK! ')
import time
time.sleep(7)
print('Primeiro me diga o que você deseja calcular? ')
time.sleep(5)
Resposta =input (' A)potencia:\n' ' B)multiplicação:\n' ' C)divisão:\n' ' D)adição:\n' ' E)subtração:\n' 'Digite uma das opções acima:   ').upper()
if Resposta[0] == 'A':
    print('Bom não é minha materia favorita, más dou um arraso:')
elif Resposta[0] == 'B':
    print('Você adora me fazer pensar né! ')
elif Resposta[0] == 'C':
    print(f'Se deseja dividir é o que faremos: ')
elif Resposta[0] == 'D':
    print('Vejo que tem bom gosto adoro uma adição:')
elif Resposta[0] == 'E':
    print('O lado bom e que subtração é bem simples de ser feita:')
else:
    print('Porfavor responda somente se deseja a letra A, B, C, D ou E, OK?')
time.sleep(4)
print('Agora que ja sabemos o que desejamos calcular vamos começar ok: ')
time.sleep(2)
P=int(input('Qual o primeiro número da operação? '))
S=int(input('Agora me diga qual o segundo número da operação? '))
time.sleep(1)
print('Eu pretendia te mostrar somente o tipo de operação que escolhesse porém\ncomo estou com ótimo humor hoje vou lhe mostrar todos os resultados, OK!')
time.sleep(4)
print(f'Potencia é {P**S}')#.format(P**S))
time.sleep(3)
print('Multiplicação é {}'.format(P*S))
time.sleep(3)
print('divisão é {}'.format(P/S))
time.sleep(3)
print('Adição é {}'.format(P+S))
time.sleep(3)
print('Subtração é {}'.format(P-S))



