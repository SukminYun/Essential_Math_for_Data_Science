import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

a = 8
b = 2

p=beta.cdf(0.90, a, b)
print(p)

x = np.linspace(0, 1, 500)
y = beta.pdf(x, a, b) #probability density function of beta distribution

#plot pdf
plt.plot(x, y) 
plt.title(f"Beta Distribution (a={a}, b={b})")
plt.xlabel("x")
plt.ylabel("pdf")
plt.grid(True)
plt.savefig('beta_pdf.png')
try:
    plt.show()
except Exception:
    pass