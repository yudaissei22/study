import numpy as np

n = 100
bins = np.linspace(0, 1, n + 1)
dist = np.digitize(3, bins)
print (dist)
