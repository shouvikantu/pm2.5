"""
"In the land of the Lorenz 63 model, three kingdoms coexist: Xeria (x), Yosha (y), and Zephyria (z). The prosperity
levels of these kingdoms are governed by the mighty constants: Sigma (σ=10), Rho (ρ=28), and Beta (β=8/3), which
control their interactions and influence on each other.

At the start of the tale, each kingdom enjoys equal prosperity, with a level of 1. As time progresses, the
 prosperity of these kingdoms ebbs and flows in a complex, chaotic dance, guided by the laws of the Lorenz 63
model. The data generated from this model represents the changes in the prosperity of these kingdoms over the
 course of 100 days, with a new chapter in the tale unfolding every 0.01 days."

"""


import numpy as np 
x,y,z  = 1,1,1

sigma, rho, beta = 10, 28, 8/3

dt = 0.01

n_steps = 10000

x_vals = np.zeros(n_steps)
y_vals = np.zeros(n_steps)
z_vals = np.zeros(n_steps)

for i in range(n_steps):
    x_vals[i] =  x
    y_vals[i] = y
    z_vals[i] =z

    dx = sigma*(y-x)*dt
    dy = (x*(rho-z)-y)*dt
    dz = (x*y - beta*z)*dt

    x += dx
    y += dy
    z+= dz



# Code to plot the code that would make some sense

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create time array for x-axis
time = np.arange(n_steps) * dt

# Create a line plot for each kingdom
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, x_vals, color='blue')
plt.title('Kingdom of Xeria')
plt.ylabel('Prosperity')

plt.subplot(3, 1, 2)
plt.plot(time, y_vals, color='green')
plt.title('Kingdom of Yosha')
plt.ylabel('Prosperity')

plt.subplot(3, 1, 3)
plt.plot(time, z_vals, color='red')
plt.title('Kingdom of Zephyria')
plt.ylabel('Prosperity')

plt.xlabel('Time (days)')
plt.tight_layout()
plt.show()

# Create a 3D plot to show the interaction between the kingdoms
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_vals, y_vals, z_vals, lw=0.5)
ax.set_xlabel("Xeria")
ax.set_ylabel("Yosha")
ax.set_zlabel("Zephyria")
ax.set_title("Interaction between Xeria, Yosha, and Zephyria")

plt.show()
