import matplotlib.pyplot as plt
import numpy as np

# Sample data
ages = np.random.randint(18, 60, size=100)  # Generating 100 random ages between 18 and 60
categories = ['Male', 'Female', 'Transgender'] 
category_counts = np.random.randint(10, 30, size=len(categories))  

# Plotting histogram
plt.subplot(2, 1, 1)
plt.hist(ages, bins=20, color='#86bf91', rwidth=0.9)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Number of People')
plt.grid(axis='y', alpha=0.75)

# Plotting bar chart
plt.subplot(2, 1, 2)
plt.bar(categories, category_counts, color='#007acc')
plt.title('Distribution of Gender')
plt.xlabel('Categories')
plt.ylabel('Number of People')

# Adjust layout to prevent overlapping
plt.tight_layout()

plt.show()
