import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Create circle
circle = Circle((0, 0), 0.5, color='blue')
ax.add_patch(circle)

# Animation function
def update(frame):
    x = frame * 0.1
    y = 0
    circle.center = (x, y)
    return circle,

# Animate
ani = FuncAnimation(fig, update, frames=100, interval=50)

plt.title("Animated Circle")
plt.show()