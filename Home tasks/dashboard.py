import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (example trend)
months = [1, 2, 3, 4, 5]
revenue = [2000, 3000, 4000, 5000, 6000]

# Create first subplot (Bar Chart)
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Category Sales")
plt.xlabel("Product Category")
plt.ylabel("Sales")

# Create second subplot (Line Plot)
plt.subplot(1, 2, 2)
plt.plot(months, revenue)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Prevent overlapping
plt.tight_layout()

# Show dashboard
plt.show()
