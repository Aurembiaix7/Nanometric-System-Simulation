#B i C) 

#Com hem vist abans el mètode de velocity Verlet i el mètode que utilitza Feynman tenen diversos canvis
#En el cas del mètode de Verlet s'ha de anar comprovant l'energia per veure que es conservi. Intentarem aportar aquesta qualitat en el cas d'en Feynman. 

import numpy as np
import matplotlib.pyplot as plt
#Equacions que descriuen l'evolució de la posició 

#Condicions inicials
xo=1.0
vo=0
m=2
g=9.8
h=20
E0=0.5*m*vo**2+m*g*h

#Dades del programa
print('\n-----------------')
print('NUMERICAL SOLUTION')
print('-------------------')
print('càlculs de Feynmann')

#time step
dt=float(input('\n Time step dt (Segons Feynmann dt=0.1s):\n> '))

#Temps final
ntot= int(input('\n Número de steps ( al voltant de 1000 steps)'))
print ('El temps de simulació serà',dt*ntot,'unitats arbitràries')

x = np.zeros(ntot+1)
vx = np.zeros(ntot+1)
t = np.zeros(ntot+1)

#Condicions inicials
t[0] = 0.0
x[0] = xo
vx[0] = vo

#Després de dt/2
a=-x[0]
V = vx[0]+(dt/2.0)*a

#Nova posició 
x[1] = x[0]+dt*vx[0]
t[1] = t[0]+dt
i=1

while i<ntot:
    print('t=', round(t[i],2), 'x=', round(x[i],2))
    #Per calcular l'acceleració a la posició actual x(t)
    a=-x[i]
    #Canvi des de t-dt/2 a t+dt/2
    V = V+a*dt
    #Nova posició
    x[i+1]=x[i]+dt*V
    #Update de temps
    t[i+1]=t[i]+dt
    i=i+1


print('Step', i, 't=',round(t[i],2), 'x=',round(x[i],2))
print('resultats')

plt.plot(t,x)
plt.xlabel('temps (ns)')
plt.ylabel('x (ns)')
plt.show()

#Plot energia
#Energia en tots els passos
E=0.5*m*vx**2+m*g*h

#Valor relatiu (E/E0)
RE=E/E0

plt.plot(t,RE)
plt.xlabel('temps (ns)')
plt.ylabel('E/E0')

plt.show()

#En el cas del càlcul que fa Feynmann hem implementat el càlcul de l'energia (cinètica i potencial) per veure si l'algoritme compleix el teorema de Noether o no.
#En els resultats, podem veure com E/E0 que seria la diferència d'energia es manté constant la qual cosa és un mètode vàlid i invariant sota l'oscil·lació temporal.
print('Invariant sota oscil·lació temporal') 