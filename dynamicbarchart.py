import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Initial data
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
marks = [50, 60, 70, 65, 80]

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    
    # Generate random updated marks
    new_marks = [random.randint(40, 100) for _ in marks]
    
    ax.bar(subjects, new_marks, color='skyblue')
    ax.set_ylim(0, 100)
    ax.set_title("Dynamic Bar Chart")
    ax.set_ylabel("Marks")

ani = animation.FuncAnimation(fig, update, interval=1000)

plt.show()