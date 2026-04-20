import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Dynamic Scatter Plot")

x_data = []
y_data = []

# Animation loop
for i in range(50):
    x_data.append(np.random.rand() * 10)
    y_data.append(np.random.rand() * 10)

    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Dynamic Scatter Plot")

    ax.scatter(x_data, y_data, color='blue')

    plt.pause(0.2)

plt.show()