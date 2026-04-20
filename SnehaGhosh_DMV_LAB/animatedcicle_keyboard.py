import matplotlib.pyplot as plt
from matplotlib.patches import Circle

x, y = 0, 0
step = 0.2

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_title("Move Circle with Arrow Keys")

circle = Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

def on_key(event):
    global x, y

    if event.key == 'up':
        y += step
    elif event.key == 'down':
        y -= step
    elif event.key == 'left':
        x -= step
    elif event.key == 'right':
        x += step

    circle.center = (x, y)
    fig.canvas.draw()

fig.canvas.mpl_connect('key_press_event', on_key)

plt.grid()
plt.show()