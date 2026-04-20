import matplotlib.pyplot as plt
import numpy as np

# Create figure with 2 subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Dynamic lines (initial empty)
line1, = axs[0].plot([], [], 'b')
line2, = axs[1].plot([], [], 'r')

# Set limits
axs[0].set_xlim(0, 10)
axs[0].set_ylim(-1.5, 1.5)
axs[0].set_title("Dynamic Sine")

axs[1].set_xlim(0, 10)
axs[1].set_ylim(-1.5, 1.5)
axs[1].set_title("Dynamic Cosine")

# Animation loop
for i in range(1, len(x)):
    line1.set_data(x[:i], np.sin(x[:i]))
    line2.set_data(x[:i], np.cos(x[:i]))

    plt.pause(0.05)

plt.show()