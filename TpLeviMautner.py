# Ejercicio 2. Construir un np.ndarray que contenga 8 nodos equiespaciados entre −1 y 1 y resolver
# el sistema lineal del ejercicio 1, obteniendo as´ı los coeficientes del polinomio buscado. Implementar una
# funci´on que reciba un par´ametro x de tipo float y devuelva p(x), el valor del polinomio en ese punto.

import numpy as np
def f(x:float) -> float:
    return 1/(1 + 25*(x**2))

def p(x:float) -> float:
    return np.dot(np.vander([x],len(x_solucion)), (x_solucion))[0]

nodos = np.linspace(-1,1,8)
A =  np.vander(nodos)
b = np.array([f(x) for x in nodos])
x_solucion = np.linalg.solve(A,b)

# Ejercicio 3. En una misma figura, graficar dentro del intervalo I:
# El gr´afico de la funci´on f y el gr´afico del polinomio p hallado.
# Los valores de f en cada uno de los nodos usados para interpolar, visualizados como puntos.
# ¿C´omo es la aproximaci´on de p a f en cada uno de los nodos? ¿Y fuera de los nodos?

import matplotlib.pyplot as plt

space  = np.linspace(-1,1,100)
plt.figure(0)

vr = [p(i.item()) for i in space]
plt.plot(space,vr)
y = 1/(1 + 25*(space**2))
plt.plot(space, y)
vr = [p(x) for x in nodos]
plt.scatter(nodos, vr, c = 'green')
plt.xlabel( "x")
plt.ylabel( "y")
plt.grid(True)
# plt.show()

# En los nodos p = f y fuera son acercan pero no son iguales.

# Ejercicio 4. Implementar una funci´on para cuantificar la aproximaci´on de p a f a partir de la siguiente
# f´ormula de distancia o error
# error(x) = |f (x) − p(x)|
# Usar esta funci´on para evaluar el error de aproximaci´on de p a f , de la siguiente manera:
# Construir un nuevo vector con 100 puntos equiespaciados dentro del intervalo I (no confundir ´estos
# con los nodos en los que interpolamos antes!).
# Evaluar la funci´on de error en cada uno de los puntos y reportar el promedio y el m´aximo de estos
# 100 errores calculados.

error_space = np.linspace(-1,1,100)
error = [abs(f(x.item())-p(x.item())) for x in error_space]
Max_error = np.max(error)
Mean_error = np.mean(error)

# print(Max_error,Mean_error)

# Ejercicio 5. Recrear la figura del ejercicio 3 pero esta vez graficando tanto a f como a p a lo largo del
# intervalo [−1,2, 1,2]. ¿C´omo es la aproximaci´on por fuera del intervalo original I?


space  = np.linspace(-1.2,1.2,100)
plt.figure(0)

vr = [p(i.item()) for i in space]
plt.plot(space,vr)
y = 1/(1 + 25*(space**2))
plt.plot(space, y)
vr = [p(x) for x in nodos]
plt.scatter(nodos, vr, c = 'green')
plt.xlabel( "x")
plt.ylabel( "y")
plt.grid(True)
# plt.show()

# Es pesima

# Ejercicio 6. Repetir los ejercicios 2, 3 y 4 esta vez tomando 16 nodos. ¿C´omo cambia el comportamiento
# de p y su aproximaci´on a f ? El error de aproximaci´on medido en el ejercicio 4, ¿mejor´o o empeor´o?

#2
nodos = np.linspace(-1,1,16)
A =  np.vander(nodos)
b = np.array([f(x) for x in nodos])
x_solucion = np.linalg.solve(A,b)

#3
space  = np.linspace(-1,1,100)
plt.figure(1)
vr = [p(i.item()) for i in space]
plt.plot(space,vr)
y = 1/(1 + 25*(space**2))
plt.plot(space, y)
vr = [p(x) for x in nodos]
plt.scatter(nodos, vr, c = 'green')
plt.xlabel( "x")
plt.ylabel( "y")
plt.grid(True)
# plt.show()

#4
error_space = np.linspace(-1,1,100)
error = [abs(f(x.item())-p(x.item())) for x in error_space]
Max_error = np.max(error)
Mean_error = np.mean(error)

# print(Max_error,Mean_error)

# La aproximacion mejora. El error maximo y promedio aumento.

# Ejercicio 7. Puede demostrarse que la interpolaci´on es ´optima si la distribuci´on de los nodos en un
# dado intervalo se corresponde con las ra´ıces de una familia de polinomios conocidos como Polinomios
# de Chebyshev. A continuaci´on queremos verificar que el error cometido en la interpolaci´on se minimiza
# utilizando ´estos nodos.
# (Opcional) Investigar como se calculan los nodos de Chebyshev e implementar una funci´on en python
# que reciba como par´ametro de entrada la cantidad de nodos que se quiere generar y devuelva los
# nodos correspondientes.
# Repetir el ejercicio 6, utilizando ocho nodos de Chebyshev y comparar los errores obtenidos con el
# caso de ocho nodos equiespaciados.
# Nodos de Chebyshev :
# [0.9807852804032304 , 0.8314696123025452 , 0.5555702330196023 ,
# 0.19509032201612833 , -0.1950903220161282 , -0.555570233019602 ,
# -0.8314696123025453 , -0.9807852804032304]


#6 

#2
nodos = [0.9807852804032304 , 0.8314696123025452 , 0.5555702330196023 ,0.19509032201612833 , -0.1950903220161282 , -0.555570233019602 ,-0.8314696123025453 , -0.9807852804032304]
A =  np.vander(nodos)
b = np.array([f(x) for x in nodos])
x_solucion = np.linalg.solve(A,b)

#3
space  = np.linspace(-1,1,100)
plt.figure(2)
vr = [p(i.item()) for i in space]
plt.plot(space,vr)
y = 1/(1 + 25*(space**2))
plt.plot(space, y)
vr = [p(x) for x in nodos]
plt.scatter(nodos, vr, c = 'green')
plt.xlabel( "x")
plt.ylabel( "y")
plt.grid(True)
# plt.show()

#4
error_space = np.linspace(-1,1,100)
error = [abs(f(x.item())-p(x.item())) for x in error_space]
Max_error = np.max(error)
Mean_error = np.mean(error)

# print(Max_error,Mean_error)

# El error maximo es mayor mientras que el promedio es menor.

import math
a = 1
b = -1
def nodos_cheby(n):
    return [.5*(a+b)+.5*(b-a)*math.cos((math.pi*(2*k-1))/(2*n)) for k in range(n)]
