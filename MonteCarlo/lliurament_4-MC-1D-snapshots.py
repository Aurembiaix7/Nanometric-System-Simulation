#Simulation of 1D Ising model
#Based on the Script of Jordi Faraudo

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

#
# Function with the interactions of the model (1D spin Ising model)
# and the solution method (Metropolis Monte Carlo)
#

def mcmove_1d(config, N, beta):
        #Loop with a size equal to spins in the system
        for i in range(N):
                    #pick a random spin: generate integer random number between 0 and N
                    a = np.random.randint(0, N)
                    ## state of spin
                    s =  config[a]
                    #calculate energy cost of flipping that spin (the % is for calculation of periodic boundary condition)
                    nb = config[(a+1)%N] + config[(a-1)%N]
                    cost = 2*s*nb
                    #flip spin or not depending on the cost and its Boltzmann factor
                    ## (acceptance probability is given by Boltzmann factor with beta = 1/kBT)
                    if cost < 0:
                        s = s*(-1)
                    elif rand() < np.exp(-cost*beta):
                        s = s*(-1)
                    config[a] = s
        # return the new configuration
        return config

#This function makes an image of the spin configurations
def configPlot1D(f, config, i, N):
        ''' This modules plts the configuration '''
        N = len(config)
        plt.bar(range(N), config, color='b', align='center') #the pcolormesh can not be used now because we have a 1D system
        plt.title('MC iteration=%d'%i);
        plt.axis('tight')
        plt.pause(0.1)

#This function calculates the energy of a given configuration for the plots of Energy as a function of T
def calcEnergy(config):
    '''Energy of a given configuration'''
    energy = 0
    for i in range(len(config)):
            S = config[i]
            nb = config[(i+1)%N] + config[(i-1)%N]
            energy += -nb*S
    return energy/2.0

#This function calculates the magnetization of a given configuration
def calcMag(config):
    '''Magnetization of a given configuration'''
    mag = np.sum(config)
    return mag
#
# MAIN PROGRAM
# Here we set initial conditions and control the flow of the simulation
#
#size of the lattice
N = 64
#Enter data for the simulation
temp = float(input("\n Please enter temperature in reduced units (suggestion 1.2): "))
msrmnt = int(input("\n Enter number of Monte Carlo iterations (suggestion 1000):"))

#Init Magnetization and Energy
step=[]
M=[]
E=[]

#Generate initial condition
config =2*np.random.randint(2, size=N)-1

#Calculate initial value of magnetization and Energy
Ene = calcEnergy(config)/(N)     # calculate average energy
Mag = calcMag(config)/(N)        # calculate average magnetisation
t=0
print('MC step=',t,' Energy=',Ene,' M=',Mag)
#Update 
step.append(t)
E.append(Ene)
M.append(Mag)

#Show initial condition
print('Initial configuration:')
print(config)
#f = plt.figure(figsize=(15, 15), dpi=80);
f = plt.figure(dpi=100)
configPlot1D(f, config, 0, N)
plt.show()

#Turn on interactive mode for plots
print("Starting MC simulation")
plt.ion()

#Perform the MC iterations
for i in range(msrmnt):
            #call MC calculation
            mcmove_1d(config, N, 1.0/temp)
            #update variables
            t=t+1                              # update MC step
            Ene = calcEnergy(config)/(N*N)     # calculate average energy
            Mag = calcMag(config)/(N*N)        # calculate average magnetisation
            #Update 
            step.append(t)
            E.append(Ene)
            M.append(Mag)

            #plot only certain configurations
            if t%10 == 0:
                print('\nMC step=',t,' Energy=',Ene,' M=',Mag)
                print(config)
                configPlot1D(f, config, t, N)

#Print end
print('\nSimulation finished after',t, 'MC steps')

#interactive plotting off
plt.ioff()

#Show final configuration
configPlot1D(f, config, t, N)
plt.show()

#Plot evolution of Energy and Magnetization during the simulation
plt.subplot(2, 1, 1)
plt.plot(step, E, 'r+-')
plt.ylabel('Energy')

plt.subplot(2, 1, 2)
plt.plot(step, M, 'b+-')
plt.ylabel('Magnetization')
plt.xlabel('MC step')

#Show the plot in screen
plt.show()



#Thermal fluctuations