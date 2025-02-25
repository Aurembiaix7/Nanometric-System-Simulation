
#MÈTODES NUMÈRICS 
#1. 

#A) Descriure les equacions que descriuen l'evolució de la posició i de la velocitat i comparar-lo amb el mètode de Verlet velocity

# El mètode que fa servir Feynmann a les seves classes és el fet d'utilitzar, com ell ho anomena: "Velocity halfway"
#D'aquesta manera, la posició serà és la posició d'abans + dt vegades la velocitat en el moment de la meitat de l'interval de temps. 
#(Codi inspirat amb el de https://github.com/jfaraudo/Numerical-Newton-examples/ )
import numpy as np
import matplotlib.pyplot as plt
#Equacions que descriuen l'evolució de la posició 

#Condicions inicials
xo=1.0
vo=0

#Dades del programa
print('\n-----------------')
print('NUMERICAL SOLUTION')
print('-------------------')
print('càlculs de Feynmann')

#time step
dt=float(input('\n Time step dt (Segons Feynmann dt=0.1s):\n> '))

#Temps final
ntot= int(input('\n Número de steps (al voltant de 1000 steps)'))
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

#ALGORITME DE VERLET 
#En el cas de Verlet, el que tenim és un algorítme anticipatiu.
#Condicions inicials

#Canvio el nom de les variables per evitar confussió. 
xe0=1.0
ve0=0
m=2
g=9.8
h=20
E0=0.5*m*ve0**2+m*g*h

#Dades del programa
print('\n-----------------')
print('NUMERICAL SOLUTION')
print('-------------------')
print('càlculs de Verlet')

#time step
du=float(input('\n Time step dt (Segons Feynmann du=0.1s):\n> '))

#Temps final
nutot= int(input('\n Número de steps (al voltant de 1000 steps)'))
print ('El temps de simulació serà',du*nutot,'unitats arbitràries')

u = np.zeros(nutot+1) #temps
xe = np.zeros(nutot+1)
ve = np.zeros(nutot+1)
ae = np.zeros(nutot+1)

#Condicions inicials
xe[0] = xe0
ve[0] = ve0

#Acceleració al temps 0
ae[0]=-xe[0]

#Evolució del temps

print('\n Calculating time evolution...')
for y in range(1, nutot+1):
    print(i)
    #Update time
    u[y] = u[y-1]+du
    #Nova posició
    xe[y]=xe[y-1]+ve[y-1]*du+(1.0/2.0)*ae[y-1]*du*du
    #Acceleració a la nove posició
    ae[y]=-xe[y]
    am=(ae[y-1]+ae[y])/2.0
    ve[y]=ve[y-1]+am*du

    #Update time
    u[y] = u[y-1]+du

print('Resultats')

plt.figure(1)

plt.subplot(211)
plt.plot(u,xe)
plt.ylabel('x (nm)')

plt.subplot(212)
plt.plot(u,ve)
plt.ylabel(' v (nm/ns)')
plt.xlabel('temps (ns)')

plt.show()


plt.plot(xe,ve)
plt.xlabel('x (nm)')
plt.ylabel('v (nm/ns)')

plt.show()

#Plot energia
#Energia en tots els passos
E=0.5*m*ve**2+m*g*h

#Valor relatiu (E/E0)
RE=E/E0
plt.plot(u,RE)
plt.xlabel('temps (ns)')
plt.ylabel('E/E0')

plt.show()

#Com podem veure, hi ha una diferència entre calcular el mateix problema com ho fa Feynman que com ho fa Verlet.
#En el cas de Verlet tenim un algoritme anticipatiu que el que fa és calcular l'acceleració a partir de (a(t)+a(t+dt))/2 i en el cas de Feynman mira la velocitat intermitja.