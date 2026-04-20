import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

# Setup plot
fig, ax = plt.subplots()
bars = ax.bar(categories, [0, 0, 0, 0, 0], color='skyblue')

ax.set_ylim(0, 35)
ax.set_title("Dynamic Bar Chart")

# Animation loop
for i in range(len(values)):
    bars[i].set_height(values[i])
    plt.pause(0.8)

plt.show()