#Sortear 1 de 4 nomes:
import random
n1=str(input('Qual o primeiro aluno? '))
n2=str(input('Qual o segundo aluno? '))
n3=str(input('Qual o terceiro aluno? '))
n4=str(input('Qual o quarto aluno? '))
L=[n1, n2, n3, n4]
E=random.choice(L)
print(f'Parabéns {E} você foi o escolhido.')

