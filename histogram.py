import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.normal(50, 10, 1000)

# Create histogram
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# Labels
plt.title("Normal Distribution Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

