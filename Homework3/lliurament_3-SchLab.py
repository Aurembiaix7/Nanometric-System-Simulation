#1
import numpy as np
import matplotlib.pyplot as plt
#Primer hem de començar definint el potencial de l'equació d'Schrödinger. En el
#cas de partícula en una caixa amb una barrera de potencial intern. 

# Barrier boundaries:
lb = 0.45
rb = 0.55

def V(x):
    if (abs(x)>= lb) or abs(x)<=rb:
       return 100.0
    elif(abs(x)>1):
        return 200.0
    else:
        return 0.0

#Discretitzar l'equació d'Schrödinger per a n punts (que tal i com hem vist a classe,
# Serà de 0 a n-1)   
def Eq(n,h,x):
    F=np.zeros([n,n])
    for i in range (0,n):
        F[i,i] = 2*((h**2)*V(x[i]+1))
        if i > 0:
            F[i,i-1] = 1
            if i < n-1:
                F[i,i+1] = 1
    return F
# Hem definit com calcular el potencial i la matriu F.
# Solució numèrica.
#Interval per calcular la funció d'ona [-L/2, L/2]
L=4
xlower = -L/2.0
xupper = L/2.0

#Discretització a l'espai.
h = 0.01

#Coordinades on la solució serà calculada.
x = np.arange(xlower,xupper+h,h)
npoints = len(x)

print('Utilitzant', npoints, 'grid point')

#Calcular la F i diagonalitzar. Cal ordenar els resultats
F=Eq(npoints,h,x)
eigenValues, eigenVectros = np.linalg.eig(F)

#Ordenar els eigenvalues
idx = eigenValues.argsort()[::-1]
w = eigenValues[idx]
vs = eigenVectros[:,idx]

#Nivells d'energia
E = (w-2)/(2.0*h**2)

#Resultat d'energies 
E = (w-2)/(2.0*h**2)
for k in range(0,5):
    print('n=',k,', E(numeric)=%.4f'%E[k])

#Funció d'ona
#Init wavefunction (empty list with npoints elements)
psi=[None]*npoints

#Calcular la funció d'ona normalitzada
for k in range(0,len(w)):
    psi[k] = vs[:,k]
    integral = h*np.dot(psi[k], psi[k])
    psi[k] = psi[k]/integral**0.5

#Gràfiques
#la funció d'ona amb x
for v in range (0,5):
    plt.plot(x,psi[v],label='Wavefunction, k='+str(v))
    plt.title('wavefunction'+ str(v) + ',E=' + '{:.4f}'.format(E[v]))
    plt.legend()
    plt.xlabel('x(a.u.)')
    plt.ylabel('Wavefunction')
    plt.show()

V_array = np.array([V(xi) for xi in x])

# Augmentar la mida de la figura
plt.figure(figsize=(12, 8))

# Graficar el potencial
plt.plot(x, V_array, 'k--', label='Potencial')

scale_factor = 0.05
# Gràficar les tres primers funcions d'ona
for v in range(2):
    scaled_psi = scale_factor* psi[v] / np.max(np.abs(psi[v])) + E[v]
    plt.plot(x, scaled_psi, label=f'ψ{v}')
    plt.axhline(y=E[v], color='r', linestyle=':', label=f'E{v}')

plt.title('Pou de potencial doble i funcions ona')
plt.xlabel('x (a.u.)')
plt.ylabel('Energia / Funció ona')
plt.legend()
plt.ylim(E[0], min(V_array))
plt.xlim()
plt.xlim(x.min(), x.max())

y_min = min(E[0], min(V_array)) - 1
y_max = max(max(V_array), max(E[2] + scale_factor * psi[2] / np.max(np.abs(psi[v])))) + 1
plt.ylim(y_min, y_max)

plt.show()

print('programa acabat')