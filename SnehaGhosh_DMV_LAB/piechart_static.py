import matplotlib.pyplot as plt

# Data
labels = ['Math', 'Physics', 'Chemistry', 'Biology']
sizes = [25, 30, 20, 25]  # Percentages
colors = ['gold', 'lightblue', 'lightgreen', 'pink']
explode = (0.1, 0, 0, 0)  # Highlight first slice

plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=90)

plt.title("Student Marks Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures pie is circular

plt.show()