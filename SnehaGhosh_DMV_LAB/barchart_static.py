import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

# Static Bar Chart
plt.bar(categories, values, color='skyblue')

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Static Bar Chart")

# Show plot
plt.show()