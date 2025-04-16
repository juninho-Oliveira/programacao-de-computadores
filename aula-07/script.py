'''
impostos = ['Mei', 'Simples']

for impostos in impostos:
    print(impostos)

frutas = ['banana', 'maça', 'manga']

for frutas in frutas:
    print(frutas)



lista_de_numeros = [12, 15, 7, 9, 27, 34]

n = int(input("Digite um valor para n: "))

for x in range(len(lista_de_numeros)) :
    
    if lista_de_numeros[x] == n:
        break 
    x += 1
if x < len(lista_de_numeros):
    print(f"{n} achado na posição {x}")
else:
    print(f"{n} Não tem na lista")


primeira = []
segunda = []

while True:
    valor = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if valor == 0:
        break
    primeira.append(valor) 
while True:
    valor = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if valor == 0:
        break
    segunda.append(valor)
terceira = []
duas_lista = primeira[:]
#duas_lista.extend(segunda)
for x in range(len(segunda)):
    duas_lista.append(segunda[x])

for x in range(len(duas_lista)):
    y = 0
    for y in range(len(terceira)):
        if duas_lista[x] == terceira[y]:
            break
        y = y + 1
    if y == len(terceira):
        terceira.append(duas_lista[x])
    x = x + 1

print ("Conteúdo da terceira lista:", terceira)

'''

i = 2
while True:
    if i % 3 == 0:
        break
    print(i)
    i += 2

count = 0
while (count < 10):
# Ponto A
    print ("Passei por aqui...", count)
    count = count + 1
# Ponto B