import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulate_logistic_growth_with_death(K=1000, P0=10, r=0.5, d=0.1, lag_phase_range=(0, 5), exp_phase_range=(5, 20),
                                        death_start_range=(20, 30), time_steps=100):
    """
    Simulates a logistic population growth curve with randomized lag, exponential, and death phases.
    
    Parameters:
        K (float): Carrying capacity (maximum population size).
        P0 (float): Initial population size.
        r (float): Growth rate.
        d (float): Death rate (rate of population decline during the death phase).
        lag_phase_range (tuple): Range for randomizing the lag phase duration (min, max).
        exp_phase_range (tuple): Range for randomizing the exponential phase duration (min, max).
        death_start_range (tuple): Range for randomizing when the death phase starts (min, max).
        time_steps (int): Number of time steps to simulate.
    
    Returns:
        pd.DataFrame: A DataFrame containing time and population size.
    """
    # Randomize lag, exponential, and death phase durations
    lag_phase = np.random.uniform(lag_phase_range[0], lag_phase_range[1])
    exp_phase = np.random.uniform(exp_phase_range[0], exp_phase_range[1])
    death_start = np.random.uniform(death_start_range[0], death_start_range[1])
    
    # Generate time points
    time = np.linspace(0, lag_phase + exp_phase + (death_start - exp_phase) + 20, time_steps)
    
    # Logistic growth with death phase
    population = []
    for t in time:
        if t < lag_phase:  # Lag phase: no growth
            P = P0
        elif t < death_start:  # Logistic growth phase
            P = K / (1 + ((K - P0) / P0) * np.exp(-r * (t - lag_phase)))
        else:  # Death phase: exponential decay
            P_death_start = K / (1 + ((K - P0) / P0) * np.exp(-r * (death_start - lag_phase)))
            P = P_death_start * np.exp(-d * (t - death_start))
            P = max(P, 0)  # Ensure population doesn't go below 0
        population.append(P)
    
    # Create DataFrame
    df = pd.DataFrame({"Time": time, "Population": population})
    return df


# Generate 100 different growth curves with death phase
np.random.seed(42)  # For reproducibility
growth_curves = []

for i in range(100):
    curve = simulate_logistic_growth_with_death(
        K=np.random.uniform(500, 1500),  # Random carrying capacity
        P0=np.random.uniform(5, 50),    # Random initial population
        r=np.random.uniform(0.2, 1.0),  # Random growth rate
        d=np.random.uniform(0.05, 0.2), # Random death rate
        lag_phase_range=(0, 5),         # Random lag phase
        exp_phase_range=(5, 20),        # Random exponential phase
        death_start_range=(20, 30)      # Random death phase start
    )
    curve["Curve_ID"] = f"Curve_{i+1}"  # Add an identifier for each curve
    growth_curves.append(curve)
#print(df)
# Combine all curves into one DataFrame
all_curves_df = pd.concat(growth_curves, ignore_index=True)

# Display the first few rows of the DataFrame
print(all_curves_df.head())

# Plot a few sample curves
sample_curves = all_curves_df[all_curves_df["Curve_ID"].isin(["Curve_1", "Curve_2", "Curve_3"])]
plt.figure(figsize=(10, 6))
for curve_id, group in sample_curves.groupby("Curve_ID"):
    plt.plot(group["Time"], group["Population"], label=curve_id)

plt.title("Sample Logistic Growth Curves with Death Phase")
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.legend()
plt.grid()
plt.show()
