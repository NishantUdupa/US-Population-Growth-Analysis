import numpy as np
import matplotlib.pyplot as plt

# Shared population data
years = np.array([1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880,
                  1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990])
population = np.array([3.9, 5.3, 7.2, 9.6, 12.9, 17.1, 23.1, 31.4, 38.6, 50.2,
                       62.9, 76.0, 92.0, 105.7, 122.8, 131.7, 150.7, 179.0, 205.0, 226.5, 248.7])  # in millions

# ----------------------------------------------------------------------------------
# Function 1: Plotting log ratio log((K - x) / x) for different carrying capacities
# ----------------------------------------------------------------------------------
t = years - years[0]
x0 = population[0]
r = 0.05
K_values = [200, 250, 300]

plt.figure()
for K in K_values:
    if K > x0:
        log_ratio = np.log((K - population) / population)
        plt.plot(t, log_ratio, label=f"K = {K}")
plt.xlabel("Year (since 1790)")
plt.ylabel(r"$\log\left(\frac{K - x}{x}\right)$")
plt.title("Log Ratio vs Time for Different K Values")
plt.legend()
plt.grid()
plt.show()

# ----------------------------------------------------------------------------------
# Function 2: Linear regression on log ratio to estimate growth rate r
# ----------------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
for K in K_values:
    valid_idx = population < K
    t_valid = t[valid_idx]
    log_ratio = np.log((K - population[valid_idx]) / population[valid_idx])

    t_mean = np.mean(t_valid)
    log_mean = np.mean(log_ratio)

    slope = np.sum((t_valid - t_mean) * (log_ratio - log_mean)) / np.sum((t_valid - t_mean) ** 2)
    intercept = log_mean - slope * t_mean

    print(f"For K = {K} million: Estimated slope = -r = {slope:.5f}, Intercept = {intercept:.5f}")

    plt.scatter(t_valid, log_ratio, label=f'Data (K={K})')
    plt.plot(t_valid, intercept + slope * t_valid, label=f'Fit (r={-slope:.5f}, K={K})')
plt.xlabel("Time (years since 1790)")
plt.ylabel("log((K - x) / x)")
plt.title("Least Squares Fit for Different K values")
plt.legend()
plt.grid(True)
plt.show()

# ----------------------------------------------------------------------------------
# Function 3: Plot x'_i / x_i vs x_i using central difference for full dataset
# ----------------------------------------------------------------------------------
pop_full = population * 1e6  # convert to individuals
h = 10
x_prime = (pop_full[2:] - pop_full[:-2]) / (2 * h)
x_i = pop_full[1:-1]
x_i_mil = population[1:-1]  # in millions for labeling

x_prime_ratio = x_prime / x_i

plt.figure(figsize=(8, 5))
plt.scatter(x_i_mil, x_prime_ratio, color='blue', label=r"$x'_i / x_i$")
plt.xlabel(r"$x_i$ (Population in millions)")
plt.ylabel(r"$x'_i / x_i$")
plt.title(r"Plot of $x'_i / x_i$ against $x_i$")
plt.grid(True)
plt.legend()
plt.show()

# ----------------------------------------------------------------------------------
# Function 4: Estimate r and K by linear regression from x'_i / x_i = r(1 - x/K)
# ----------------------------------------------------------------------------------
y = x_prime_ratio
x = population[1:-1]

x_mean = np.mean(x)
y_mean = np.mean(y)

slope = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
intercept = y_mean - slope * x_mean

r_est = intercept
K_est = -r_est / slope

print(f"Estimated r: {r_est:.5f}")
print(f"Estimated K: {K_est:.2f} million")

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label="Data")
plt.plot(x, r_est * (1 - x / K_est), color='red', label=f"Fit: r={r_est:.5f}, K={K_est:.2f}")
plt.xlabel(r"$x_i$ (Population in millions)")
plt.ylabel(r"$x'_i / x_i$")
plt.title(r"Least Squares Fit for $\frac{x'_i}{x_i} = r(1 - x/K)$")
plt.legend()
plt.grid(True)
plt.show()

# ----------------------------------------------------------------------------------
# Function 5: Repeating estimation on recent data only (1950–1990)
# ----------------------------------------------------------------------------------
recent_years = np.array([1950, 1960, 1970, 1980, 1990])
recent_pop = np.array([150.7, 179.0, 205.0, 226.5, 248.7])
recent_derivative = np.array([(recent_pop[i + 1] - recent_pop[i - 1]) / (2 * h) for i in range(1, len(recent_pop) - 1)])
recent_x = recent_pop[1:-1]
recent_ratio = recent_derivative / recent_x

x_mean_r = np.mean(recent_x)
y_mean_r = np.mean(recent_ratio)

slope_r = np.sum((recent_x - x_mean_r) * (recent_ratio - y_mean_r)) / np.sum((recent_x - x_mean_r) ** 2)
intercept_r = y_mean_r - slope_r * x_mean_r

r_recent = intercept_r
K_recent = -r_recent / slope_r

print(f"New Estimated r: {r_recent:.5f}")
print(f"New Estimated K: {K_recent:.2f} million")

plt.figure(figsize=(8, 5))
plt.scatter(recent_x, recent_ratio, color='blue', label="Data")
plt.plot(recent_x, r_recent * (1 - recent_x / K_recent), color='red', label=f"Fit: r={r_recent:.5f}, K={K_recent:.2f}")
plt.xlabel(r"$x_i$ (Population in millions)")
plt.ylabel(r"$x'_i / x_i$")
plt.title(r"Least Squares Fit for $\frac{x'_i}{x_i} = r(1 - x/K)$ (Recent Data)")
plt.legend()
plt.grid(True)
plt.show()
