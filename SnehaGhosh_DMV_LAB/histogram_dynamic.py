import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randn(1000)

# Create figure
fig, ax = plt.subplots()

# Histogram bins
bins = 20

ax.set_title("Dynamic Histogram")
ax.set_xlim(-4, 4)

# Build histogram dynamically
for i in range(50, len(data), 50):
    ax.clear()
    ax.set_title("Dynamic Histogram")

    ax.hist(data[:i], bins=bins, color='orange', edgecolor='black')
    ax.set_xlim(-4, 4)

    plt.pause(0.2)

plt.show()