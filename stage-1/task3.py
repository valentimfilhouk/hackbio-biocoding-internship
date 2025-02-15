import numpy as np

def time_to_reach_80_percent(K, P0, r, lag_phase=0):
    """
    Calculate the time it takes to reach 80% of the carrying capacity in a logistic growth model.
    
    Parameters:
        K (float): Carrying capacity (maximum population size).
        P0 (float): Initial population size.
        r (float): Growth rate.
        lag_phase (float): Duration of the lag phase (default is 0).
    
    Returns:
        float: Time to reach 80% of the carrying capacity.
    """
    # Define the target population (80% of K)
    target_population = 0.8 * K
    
    # Solve for t using the derived formula
    numerator = (1 / 0.8) - 1
    denominator = (K - P0) / P0
    exponent = numerator / denominator
    
    # Avoid division by zero or invalid logarithms
    if exponent <= 0:
        raise ValueError("Invalid parameters: Check K, P0, and r values.")
    
    t = lag_phase - (1 / r) * np.log(exponent)
    return t


# Example Usage
K = 1000       # Carrying capacity
P0 = 10        # Initial population
r = 0.5        # Growth rate
lag_phase = 2  # Lag phase duration

time_80_percent = time_to_reach_80_percent(K, P0, r, lag_phase)
print(f"Time to reach 80% of carrying capacity: {time_80_percent:.2f} time units")
