import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Initial labels and data
labels = ['A', 'B', 'C', 'D']
data = [25, 25, 25, 25]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    
    # Generate random data that sums to 100
    new_data = [random.randint(5, 50) for _ in data]
    total = sum(new_data)
    new_data = [d * 100 / total for d in new_data]
    
    ax.pie(new_data, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Dynamic Pie Chart")

ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()