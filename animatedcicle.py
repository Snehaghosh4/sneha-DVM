import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle, = ax.plot([], [], 'bo', markersize=20)

def update(frame):
    x = 5 + 3 * np.cos(frame)
    y = 5 + 3 * np.sin(frame)
    circle.set_data([x], [y])
    return circle,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 2*np.pi, 100),
    interval=50,
    repeat=True
)

plt.show() 