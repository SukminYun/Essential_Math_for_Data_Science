from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n = 10  # trial
p = 0.9  # probability

k = np.arange(n + 1) #making the array (0 to n successes)
pmf = binom.pmf(k, n, p)  # the probability mass function of binomial distribution

for ki, prob in zip(k, pmf):
    print(f"{ki} - {prob}")

# Plot PMF
plt.figure(figsize=(8, 4))
plt.bar(k, pmf, color='C0', alpha=0.8)
plt.xlabel('k')
plt.ylabel('PMF')
plt.title(f'Binomial PMF (n={n}, p={p})')
plt.xticks(k)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
# Save image so it's viewable in headless environments
plt.savefig('binomial_pmf.png')
try:
    plt.show()
except Exception:
    pass


