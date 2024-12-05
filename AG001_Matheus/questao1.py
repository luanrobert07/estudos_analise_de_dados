#Importação
from sympy import Limit, Symbol, sqrt, oo, S

c = 160%10

#Definindo x
x = Symbol('x')

#Definindo função.
def Funcao(x):
    return ((2*(x**2) - 7)/(7*(x**5) - 2)) * (c + 1)

#Limite da função quando x -> 1
Resultado1 = Limit(Funcao(x), x, 1).doit()
print ('\n Limite da função para x -> 1.')
print (Resultado1)
#Limite da função quando x -> oo
Resultado2 = Limit(Funcao(x), x, S.Infinity).doit()
print ('\n Limite da função para x -> oo.')
print (Resultado2)
#Limite da função quando x -> -oo
Resultado3 = Limit(Funcao(x), x, -S.Infinity).doit()
print ('\n Limite da função para x -> -oo.')
print (Resultado3)