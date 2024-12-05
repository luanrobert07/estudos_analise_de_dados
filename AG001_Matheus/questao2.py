#Importação
from sympy import Integral, Derivative, Symbol

c = 163 % 10

#Definindo x
t = Symbol('t')

#Definindo função
def V(t):
    return 5*c + 7*(t**4) + t**(1/3) - 3*c*(t**3)

#Equação do deslocamento
Deslocamento = Integral(V(t), t).doit()

print ('\n Equação do Deslocamento.')
print (Deslocamento)

#Deslocamento de t = 1s a t = 7s.
Resultado = (Integral(V(t), t).doit().subs({t:7})) - (Integral(V(t), t).doit().subs({t:1}))

print ('\n Deslocamento de t = 1s a t = 7s.')
print (Resultado)

#Equação da aceleração
Aceleracao = Derivative(V(t), t).doit()

print ('\n Equação da aceleração.')
print (Aceleracao)