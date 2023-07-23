import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Lorenz 96 model parameters
F = 10
b = 10 

# Number of variables
J = 40  

# Initialize X array
X = np.zeros(J)  

# Timestep  
dt = 0.01

# Main loop
timesteps = 10000
X_data = []
for t in range(timesteps):

    # Calculate dX/dt
    dX_dt = np.zeros(J)
    dX_dt[:-1] = (X[1:] - X[:-1]) * X[1:] - X[:-1] + F
    dX_dt[-1] = (X[0] - X[-1]) * X[0] - X[-1] + F

    # Integrate forward in time
    X += dt * dX_dt

    # Sample data
    if t % 10 == 0:
        X_sample = X.copy()  # Make a copy to avoid overwriting X
        X_data.append(X_sample)

# Convert to Pandas dataframe  
X_df = pd.DataFrame(X_data)

# Save to CSV file
X_df.to_csv("simulated_data.csv", index=False)

#PLotting 


X_df = pd.read_csv("simulated_data.csv")

# Get the number of variables (J) and the number of timesteps
J = X_df.shape[1]
timesteps = X_df.shape[0]

# Create an array for time steps
time_steps = np.arange(timesteps) * dt

# Plot the evolution of each variable
plt.figure(figsize=(12, 6))
for j in range(J):
    plt.plot(time_steps, X_df.iloc[:, j], label=f'Variable {j+1}')

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Evolution of Lorenz 96 System Variables')
plt.legend()
plt.show()