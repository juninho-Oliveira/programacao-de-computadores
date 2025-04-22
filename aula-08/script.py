'''
   1. Escreva uma função que retorne o maior valor entre dois números.
Valores esperados:
maximo(5,6) = 6
maximo (12,12) = 12


def RetorneMaiorValor(N1, N2):
    if(N1>N2):
        print("N1 é maior que N2", N1)
    else:
        print("N2 é maior que N1", N2)

RetorneMaiorValor(20,3)

'''

'''
2. Escreva uma função que receba dois números e retorne True se o primeiro número for
múltiplo do segundo.
Valores esperados:
multiplo(8,4) = True
multiplo (7,3) = False



def RetorneTrueMultiplo(N1, N2):
    valor = N2 * 2
    if(valor == N1):
        print(True)
    else:
        print(False)

RetorneTrueMultiplo(7,3)

RetorneTrueMultiplo(8,4)

'''

'''
3. Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado2).
Valores esperados:
area_quadrado(4) = 16
area_quadrado (9) = 81
78 

def Area(A):
    lado = A
    valor = A * lado
    print(valor)

Area(9)
'''
