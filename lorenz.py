from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Lorenz paramters and initial conditions
N = 5
F = 8

def lorenz(x,t):
    xdot = np.zeros(N)
    for i in range(N):
        xdot[i] = (x[(i+1)%N]-x[i-2]) * x[i-1] - x[i] + F
    return xdot

x0 = np.ones(N)
x0[0] += 0.01 # add small perturbation to the first variable
t = np.arange(0.0, 30.0, 0.01)

x=odeint(lorenz, x0, t)

# Plot the Lorenz attractor using a Matplotlib 3D projection

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot(x[:,0], x[:,1], x[:,2])
plt.show()