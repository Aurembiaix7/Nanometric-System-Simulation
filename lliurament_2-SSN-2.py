#2
#Càlcul amb l'equació d'Schrödinger.
import numpy as np
import matplotlib as plt

# Constants en unitats SI
h_bar = 1.054571817e-34  # Constant de Planck reduïda (J·s)
m = 9.10938356e-31  # Massa de l'electró (kg)
k = 1e10  # nombre d'ona (m^-1)

import numpy as np

# Constants en unitats SI
h_bar = 1.054571817e-34  # Constant de Planck reduïda (J·s)
m = 9.10938356e-31  # Massa de l'electró (kg)
k = 1e10  # Nombre d'ona (m^-1)

# Funció d'ona plana (només espacial)
def psi_SI(x):
    return np.exp(1j * k * x)

# Equació de Schrödinger (només part espacial)
def schrodinger_SI_spatial(psi, x):
    return (h_bar**2 / (2 * m)) * np.gradient(np.gradient(psi, x), x)

# Crear valors per a x
x = np.linspace(0, 1e-9, 100)  # 100 punts entre 0 i 1 nanòmetre

# Calcular la funció d'ona
psi = psi_SI(x)

# Imprimir resultats
print("Funció d'ona per als primers 5 punts x:")
print(psi[:5])

# Calcular l'equació de Schrödinger (només part espacial)
schrodinger_result = schrodinger_SI_spatial(psi, x)

print("\nResultat de l'equació de Schrödinger (part espacial) per als primers 5 punts x:")
print(schrodinger_result[:5])

# En unitats atòmiques
h_bar = m = 1
k = 1  # Vector d'ona (en unitats atòmiques)

# Funció d'ona plana
def psi_atomic(x):
    return np.exp(1j * (k * x))

# Equació de Schrödinger
def schrodinger_atomic(psi, x):
    return (h_bar**2 / (2 * m)) * np.gradient(np.gradient(psia, x), x)
   
# Crear valors per a x i t
x = np.linspace(0, 10, 100)  # 100 punts entre 0 i 10 unitats atòmiques de longitud

# Calcular la funció d'ona
psia = psi_atomic(x)

# Imprimir resultats
print("Funció d'ona per als primers 5 punts x:")
print(psia[:5])

# Calcular l'equació de Schrödinger
schrodinger_result = schrodinger_atomic(psi, x)

print("\nResultat de l'equació de Schrödinger per als primers 5 punts x")
print(schrodinger_result[:5])