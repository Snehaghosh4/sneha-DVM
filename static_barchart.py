import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

# Create bar chart
plt.bar(categories, values, color='green')

# Labels and Title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Static Bar Chart")

# Show the graph
plt.show()