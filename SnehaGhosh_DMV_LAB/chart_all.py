import pandas as pd
import matplotlib.pyplot as plt

# -------- CREATE DATASET --------
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 25, 15, 30, 20]
}

df = pd.DataFrame(data)

# -------- CREATE SUBPLOTS --------
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
fig.suptitle("Dataset Visualization using Matplotlib & Pandas")

# -------- BAR CHART --------
axs[0, 0].bar(df['Category'], df['Values'], color='skyblue')
axs[0, 0].set_title("Bar Chart")

# -------- LINE CHART --------
axs[0, 1].plot(df['Category'], df['Values'], marker='o', color='green')
axs[0, 1].set_title("Line Chart")

# -------- PIE CHART --------
axs[0, 2].pie(df['Values'], labels=df['Category'], autopct='%1.1f%%')
axs[0, 2].set_title("Pie Chart")

# -------- STAIR PLOT --------
axs[1, 0].step(df['Category'], df['Values'], where='mid', color='purple')
axs[1, 0].set_title("Stair Plot")

# -------- HISTOGRAM --------
axs[1, 1].hist(df['Values'], bins=5, color='orange', edgecolor='black')
axs[1, 1].set_title("Histogram")

# Hide empty subplot
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()