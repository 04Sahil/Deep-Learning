import numpy as np
from matplotlib.pyplot import subplots
fig, ax = subplots(figsize=(8, 8))
rng = np.random.default_rng(1303)
print(rng.normal(scale=5, size=2))
x = rng.standard_normal(100)
y = rng.standard_normal(100)
ax.plot(x, y)