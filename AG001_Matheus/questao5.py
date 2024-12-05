#Importação
from sympy import Symbol, solve, exp, sin

c = 160%10

#Define x como uma variável.
x = Symbol('x')

#Define uma nova função.
def Funcao1(x):
    return exp(x-3) + exp(x-1) + exp(x) - (c+1)

#Resolve a equação Funcao1 = 0.
y1 = Funcao1(x)

Resultado = solve (y1)

print ('\n Resultado da equação 1')
print ('x =', Resultado)

#Define uma nova função.
def Funcao2(x):
    return x**4 - 4*(x**3) + 3*x - c

#Resolve a equação Funcao2 = 0.
y2 = Funcao2(x)

Resultado = solve (y2)

print ('\n Resultado da equação 2')
print ('x =', Resultado)

#Define uma nova função.
def Funcao3(x):
    return 4*sin((c+1)*x) + 2

#Resolve a equação Funcao3 = 0.
y3 = Funcao3(x)

Resultado = solve (y3)

print ('\n Resultado da equação 3')
print ('x =', Resultado)