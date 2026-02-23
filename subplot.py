import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = x**2

# Create a 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# First subplot
axes[0, 0].plot(x, y1, 'r')
axes[0, 0].set_title("Sine Wave")

# Second subplot
axes[0, 1].plot(x, y2, 'g')
axes[0, 1].set_title("Cosine Wave")

# Third subplot
axes[1, 0].plot(x, y3, 'b')
axes[1, 0].set_title("Tangent Wave")
axes[1, 0].set_ylim(-10, 10)  # limit extreme values

# Fourth subplot
axes[1, 1].plot(x, y4, 'm')
axes[1, 1].set_title("Quadratic")

plt.tight_layout()  # Adjust spacing
plt.show()
