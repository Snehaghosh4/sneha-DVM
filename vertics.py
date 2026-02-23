import matplotlib.pyplot as plt
import math

while True:
    try:
        n = int(input("Enter number of vertices (>=3): "))
        if n >= 3:
            break
        else:
            print("Number must be at least 3.")
    except ValueError:
        print("Please enter a valid integer.")

# Calculate positions of vertices in a circle
radius = 5
center_x, center_y = 0, 0
angles = [2 * math.pi * i / n for i in range(n)]
vertices = [(center_x + radius * math.cos(a), center_y + radius * math.sin(a)) for a in angles]

# Draw edges (connect every pair of vertices)
plt.figure(figsize=(6,6))
for i in range(n):
    for j in range(i+1, n):
        x_values = [vertices[i][0], vertices[j][0]]
        y_values = [vertices[i][1], vertices[j][1]]
        plt.plot(x_values, y_values, color='gray')

# Draw vertices
for i, (x, y) in enumerate(vertices):
    plt.scatter(x, y, color='skyblue', s=200)
    plt.text(x, y, str(i+1), fontsize=12, ha='center', va='center')

plt.title(f"Complete Graph with {n} vertices")
plt.axis('off')  # Hide axes
plt.show()
