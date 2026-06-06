import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

ave = 60
std = 10

x = np.linspace(ave - 4 * std, ave + 4 * std, 1000)
pdf = norm.pdf(x, ave, std)

#plot pdf
plt.plot(x, pdf) 
plt.title(f"Normal Distribution (average={ave}, std={std})")
plt.xlabel("x")
plt.ylabel("pdf")
plt.grid(True)
plt.savefig('norm_pdf.png')
try:
    plt.show()
except Exception:
    pass