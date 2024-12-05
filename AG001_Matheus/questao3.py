#Importação
from sympy import Integral, Symbol

c = 163 % 10

#Definindo x
x = Symbol('x')

#Definindo função
def F(x):
    return 5*(x**3) + (x/3)**(3/5) + (3/4)*x - 3*c

#Trabalho da força para x entre 3m e 8m.
Trabalho = Integral(F(x), (x, 3, 8)).doit()

print ('\n Trabalho sobre o objeto entre x = 3m e x = 8m.')
print (Trabalho)