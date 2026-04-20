import matplotlib.pyplot as plt
import numpy as np

plt.ion()

num_points = int(input("Number of points: "))
x_min = int(input("X-axis minimum: "))
x_max = int(input("X-axis maximum: "))
y_min = int(input("Y-axis minimum: "))
y_max = int(input("Y-axis maximum: "))
pause_time = float(input("Pause time (seconds): "))

fig, ax = plt.subplots()
x_data, y_data = [], []

for _ in range(num_points):
    x_data.append(np.random.randint(x_min, x_max))
    y_data.append(np.random.randint(y_min, y_max))

    ax.clear()
    ax.scatter(x_data, y_data, color='green')
    ax.set_xlim(x_min, x_max + 10)
    ax.set_ylim(y_min, y_max + 10)
    ax.set_title("Dynamic Scatter Plot (User Controlled)")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    plt.pause(pause_time)

plt.ioff()
plt.show()
