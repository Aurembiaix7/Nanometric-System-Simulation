# Simulation of 2D Ising model
#Based on the Script of Jordi Faraudo
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

# Generate a random initial state for N spins in 1D
def initialstate_1d(N):
    '''Generates a random spin configuration for initial condition in 1D'''
    state = 2 * np.random.randint(2, size=N) - 1
    return state

# Monte Carlo move using Metropolis algorithm for 1D Ising model
def mcmove_1d(config, beta):
    '''Monte Carlo move using Metropolis algorithm in 1D'''
    N = len(config)
    for i in range(N):
        # Select a random spin
        a = np.random.randint(0, N)
        s = config[a]
        # Calculate energy cost of flipping this spin (periodic boundary conditions)
        nb = config[(a + 1) % N] + config[(a - 1) % N]
        cost = 2 * s * nb
        # Flip spin with Metropolis criterion
        if cost < 0 or np.random.rand() < np.exp(-cost * beta):
            config[a] *= -1
    return config

# Calculate the energy of a given configuration in 1D
def calcEnergy_1d(config):
    '''Energy of a given configuration in 1D'''
    N = len(config)
    energy = 0
    for i in range(N):
        S = config[i]
        nb = config[(i + 1) % N]  # Only one neighbor (periodic boundary)
        energy += -nb * S
    return energy / 2.0

# Calculate the magnetization of a given configuration in 1D
def calcMag_1d(config):
    '''Magnetization of a given configuration in 1D'''
    mag = np.sum(config)
    return mag

# Main program parameters
nt = 2**8         # number of temperature points
N = 2**6          # size of the lattice (number of spins)
eqSteps = 2**10   # number of MC sweeps for equilibration
mcSteps = 2**10   # number of MC sweeps for calculation

n1, n2 = 1.0 / (mcSteps * N), 1.0 / (mcSteps * mcSteps * N)
tm = 2.269; T = np.random.normal(tm, .64, nt)
T = T[(T > 0.5) & (T < 5.0)]; nt = np.size(T)

Energy = np.zeros(nt)
Magnetization = np.zeros(nt)
SpecificHeat = np.zeros(nt)
Susceptibility = np.zeros(nt)

# Simulation loop
print('Starting Simulations at', len(T), 'different temperatures.')
for m in range(len(T)):
    E1 = M1 = E2 = M2 = 0
    config = initialstate_1d(N)
    iT = 1.0 / T[m]
    iT2 = iT * iT
    print('Simulation', m + 1, 'of', len(T), 'at reduced temperature T=', T[m])

    for i in range(eqSteps):         # Equilibrate system
        mcmove_1d(config, iT)

    for i in range(mcSteps):         # Perform measurements
        mcmove_1d(config, iT)
        Ene = calcEnergy_1d(config)     # Calculate energy
        Mag = calcMag_1d(config)       # Calculate magnetization

        E1 += Ene
        M1 += Mag
        M2 += Mag * Mag
        E2 += Ene * Ene

        Energy[m]         = n1 * E1
        Magnetization[m]  = n1 * M1
        SpecificHeat[m]   = (n1 * E2 - n2 * E1 * E1) * iT2
        Susceptibility[m] = (n1 * M2 - n2 * M1 * M1) * iT
#Plot
f = plt.figure(figsize=(18, 10)); # plot the calculated values

sp =  f.add_subplot(2, 2, 1 );
plt.plot(T, Energy, 'o', color="#A60628");
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Energy ", fontsize=20);

sp =  f.add_subplot(2, 2, 2 );
plt.plot(T, abs(Magnetization), 'o', color="#348ABD");
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Magnetization ", fontsize=20);

sp =  f.add_subplot(2, 2, 3 );
plt.plot(T, SpecificHeat, 'o', color="#A60628");
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Specific Heat ", fontsize=20);

sp =  f.add_subplot(2, 2, 4 );
plt.plot(T, Susceptibility, 'o', color="#348ABD");
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Susceptibility", fontsize=20);
plt.show()