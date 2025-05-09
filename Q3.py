import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = -x**2 + 2*x + 8

# Plotting
plt.plot(x, y)
plt.title("y = -x² + 2x + 8")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# Finding the maximum value of y
print("Maximum value of y:")
print(np.max(y))
