 # PROGRAMA - LE DOIS VALORES E IMPRIME QUAL É O MAIOR

''' a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

if a > b:
	print ("O primeiro valor é o maior ")
if b > a:
	print("O segundo valor é o maior")
if a==b:
	print("Os numeros são iguais") 

# EXEMPLO - CARRO NOVO OU VELHO, DEPENDENDO DA IDADE:

idade = int(input("Digite a idade do seu carro: "))
if (idade <= 3):
    print("Seu carro é novo")
else: 
	print("Seu carro é velho")


# EXEMPLO - CONTA DE TELEFONE COM TRÊS FAIXAS DE PREÇO
minutos = int(input("Quantos minutos foram utilizados no mês: "))
preco = int(0)
if minutos < 200:
    preco = 0.20
else: 
    if minutos < 400:
        preco = 0.18
    else: 
        preco = 0.15
print(f"Você vai pagar esse mês: R$ {minutos*preco:6.2f}")



# EXEMPLO 7 - categoria x preço

categoria = int(input("Digite a categoria do produto: "))
preco = int(0)
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
	preco = 31
else:
     print("Categoria invalida, digite um valor entre 1 e 5!")
print(f"O preço do produto é: R$ {preco:6.2f}")


import math

valor = int(input("Digite o valor: "))

print(f"Valor: {math.sqrt(valor)}")



contador = 1
while(contador <= 5):
    x = int(input("Digite um valor para x: "))
    r = x * 3
    print("O valor de R é:", r)
    contador = contador + 1


contador = 1
resposta = "sim"
while(resposta == "sim" or resposta == "s"):
    x = int(input("Digite um valor para x: "))
    r = x * 3
    print("O valor de R é:", r)
    resposta = input("Deseja continuar ?")
    
'''

fatorial = contador = 1
while (contador <= 5):
    fatorial = fatorial * contador
    contador = contador + 1
print ("O fatorial de 5 é: ", fatorial)
nome = ""
input(nome)


