#Ordenamiento por inserción
import random

def Insercion(numeros):
    for a in range(1,len(numeros)):
        valor=numeros[a]
        i=a-1
        while i>=0:
            if valor<numeros[i]:
                numeros[i+1]=numeros[i]
                numeros[i]=valor
                i=i-1
            else:
                break
            
tam = 10
Numeros = list()
for i in range(tam):
    Numeros.append(random.randint(1,100))
print(Numeros)
Insercion(Numeros)
print(Numeros)
            
