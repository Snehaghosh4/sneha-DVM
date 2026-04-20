import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create figure
fig, ax = plt.subplots()

# Empty line
line, = ax.plot([], [], color='blue')

# Axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Animated Line Graph")

# Initialize
def init():
    line.set_data([], [])
    return line,

# Update function
def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

# Animation
ani = FuncAnimation(fig, update,
                    frames=len(x),
                    init_func=init,
                    interval=50,
                    blit=True)

plt.show()