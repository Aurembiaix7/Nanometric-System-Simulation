#La idea és realitzar el càlcul dels moments principals d'inèrcia per a diferents casos de tres dimensions. 
#En el cas que els moments principals d'inèrcia siguin diferents (valors propis), que l'script pugui dissernir entre
#- Un cas esfèric (Tots els valors propis són iguals)
#- Un cas simètric (Dos dels valors propis són iguals)
#- Un cas asimètric (Tots els valors propis són diferents entre ells)

import numpy as np

I_1=np.array([[2,1,0],[1,2,0],[0,0,1]])
print('Primer tensor')
print(I_1)
Eigenvalue1,Eigenvector= np.linalg.eig(I_1)
print('Eigenvalue 1')
print(Eigenvalue1)

#Per ordenar els eigenvalues
idx1 = Eigenvalue1.argsort()[::-1]
Eigenvalue1x = Eigenvalue1[idx1]

print('\nMoments principals de inèrcia  ordenats 1:') 
for k, eigenvalue in enumerate(Eigenvalue1, 1):
    print(f'Eigenvalue {k}: {eigenvalue:.4f}') #Només per agafar els 4 primers decimals en cada cas.

#rounded_eigenvalues1=np.round(Eigenvalue1,decimals=3)
#Per poder evitar els errors dels eigenvalues els arrodonim. Així podrem determinar si són els mateixos o no.

# Classificació de la baldufa
if np.allclose(Eigenvalue1, Eigenvalue1[0]):
    print('Tipus: Baldufa esfèrica')
elif np.sum(Eigenvalue1 == Eigenvalue1[0]) == 2 or np.sum(Eigenvalue1 == Eigenvalue1[1]) == 2:
    print('Tipus: Baldufa simètrica')
else:
    print('Tipus: Baldufa asimètrica')

print('......................................')

I_2= np.array([[2,0,0],[0,2,0],[0,0,2]])
print('Segon tensor')
print(I_2)
Eigenvalue2,Eigenvector= np.linalg.eig(I_2)
print('Eigenvalue 2')
print(Eigenvalue2)

#Per ordenar els eigenvalues
idx2 = Eigenvalue2.argsort()[::-1]
Eigenvalue2x = Eigenvalue2[idx2]

print('\nMoments principals de inèrcia  ordenats 2:')
for k, eigenvalue in enumerate(Eigenvalue2, 1):
    print(f'Eigenvalue {k}: {eigenvalue:.4f}')

# Classificació de la baldufa
if np.allclose(Eigenvalue2, Eigenvalue2[0]):
    print('Tipus: Baldufa esfèrica')
elif np.sum(Eigenvalue2 == Eigenvalue2[0]) == 2 or np.sum(Eigenvalue2 == Eigenvalue2[1]) == 2:
    print('Tipus: Baldufa simètrica')
else:
    print('Tipus: Baldufa asimètrica')


print('......................................')
I_3=np.array([[20,-5,2],[-5,25,-3],[2,-3,18]]) #Nota: Poden ser negatius perquè són el producte d'inèrcia! Que no és el mateix que moment d'inèrcia.
print('Tercer tensor')
print(I_3)
Eigenvalue3,Eigenvector= np.linalg.eig(I_3)
print('Eigenvalue 3')
print(Eigenvalue3)

#Per ordenar els eigenvalues
idx3 = Eigenvalue3.argsort()[::-1]
Eigenvalue3x = Eigenvalue3[idx3]

print('\nMoments principals de inèrcia  ordenats 3:')
for k, eigenvalue in enumerate(Eigenvalue3, 1):
    print(f'Eigenvalue {k}: {eigenvalue:.4f}')

# Classificació de la baldufa
if np.allclose(Eigenvalue3, Eigenvalue3[0]):
    print('Tipus: Baldufa esfèrica')
elif np.sum(Eigenvalue3 == Eigenvalue3[0]) == 2 or np.sum(Eigenvalue3 == Eigenvalue3[1]) == 2:
    print('Tipus: Baldufa simètrica')
else:
    print('Tipus: Baldufa asimètrica')

