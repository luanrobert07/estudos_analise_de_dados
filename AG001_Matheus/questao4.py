#Importação
from sympy import Symbol, solve

c = 163 % 10

#Definindo as correntes I1, I2 e I3
I1 = Symbol('I1')
I2 = Symbol('I2')
I3 = Symbol('I3')

#Definindo funções.
def Funcao1(I1,I2):
    return -(7 + (5*c)) + I1*15000 + (4 + 2*c) + I2*5000

def Funcao2(I2,I3):
    return I3*10000 + (3 + 4*c) - I2*5000

def Funcao3(I1,I2,I3):
    return -I1 + I2 + I3

#Resolvendo o sistema.
f = Funcao1(I1,I2)
g = Funcao2(I2,I3)
h = Funcao3(I1, I2, I3)

Resultado = solve ((f,g,h))

print ('\n Resultado do sistema de equações.')
print (Resultado)