# U.S. Population Growth Analysis

This project analyzes historical U.S. population data (1790–1990) using logistic growth modeling, central difference derivatives, and least-squares regression. It combines analytical modeling and numerical methods to estimate key growth parameters and evaluate how population trends have evolved over time.

## What It Does

- **Logistic Model Exploration**: Visualizes \( \log\left(\frac{K - x}{x}\right) \) for various carrying capacities \( K \) to understand saturation dynamics.
- **Growth Rate Estimation**: Applies linear regression to estimate the intrinsic growth rate \( r \) from transformed population data.
- **Derivative Analysis**: Uses the central difference method to estimate \( x' \) and plot \( \frac{x'}{x} \) against population for growth insight.
- **Parameter Fitting**: Fits the logistic model \( \frac{x'}{x} = r(1 - \frac{x}{K}) \) to the full dataset and to modern data (1950–1990).
- **Trend Comparison**: Compares historical and modern estimates of \( r \) and \( K \) to assess changes in population dynamics.

## Results Summary

| Time Range     | Estimated \( r \) | Estimated \( K \) (millions) |
|----------------|------------------|-------------------------------|
| Full Dataset   | 0.0291           | 288.88                        |
| 1950–1990 Only | 0.0359           | 307.23                        |
| Assumed K = 200–300 | \( r \) ≈ 0.028–0.035 | —                       |

These results suggest the U.S. population followed logistic growth with increasing capacity over time, likely reflecting improvements in infrastructure, healthcare, and resource availability post-1950.

## Requirements

- Python 3
- NumPy
- Matplotlib
