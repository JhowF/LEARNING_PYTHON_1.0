#'FOR' usado sempre que ouver processo repetitivo no programa
#for = for each = PARA CADA item num conjunto de item.

Lista_produtos = ['faca','garfo','panela','frigideira','flavorstone']
for anything in Lista_produtos:
    print(anything.capitalize())
    print(anything.replace('panela', 'jonathan'))


#ENTENDENDO MELHOR O FOR

Lista_precos = [10,20,30,40,50,60,70,80]
for preco in Lista_precos :
    imposto = preco * 0.1
    print (imposto)

#RANGE - vai execultar conforme a quantidade dentro do ranger.

for item in range (5):
    print (item)
    print('Jonathan gato')

with open('Python.txt','r') as arquivo :
    texto = arquivo.read()
    Lista_texto = texto [320:]
    print(Lista_texto.split())
    #print(len(texto))
    #Lista_texto = texto [320:]
    #print(Lista_texto)

