import numpy as np
import matplotlib.pyplot as plt


sims = 10000000

A = np.random.uniform(1, 5, sims) #uniform distribution 1-5 hours
B = np.random.uniform(2, 6, sims)

duration = A + B

plt.figure(figsize = (3, 1.5))
plt.hist(duration, density = True) # Plot in form of probab density
plt.axvline(9, color = 'r') # Party starts after 9 hours
plt.show()

print((duration > 9).sum()/sims)
