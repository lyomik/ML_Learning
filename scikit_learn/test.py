import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

x = np.random.randint(0, 100, 50)

y = x + np.random.normal(0, 10, 50)

coef = np.corrcoef(x, y)
print(coef)
plt.scatter(x, y)
plt.show()