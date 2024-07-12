# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import random
# fig, ax = plt.subplots()
# li = [random.randint(1, 50) for _ in range(4)]
# print(li)
# def animate(i):
#     ax.clear()
#     li = [random.randint(1, 50) for _ in range(4)]
#     plt.bar([1,2,3,4], li)
#     plt.xlabel("X axis")
#     plt.ylabel("Y axis")
#     plt.title("Animate")
     
# ani = animation.FuncAnimation(fig, animate, frames=100, interval = 1000, blit = False)
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd 
import os

# Get the current working directory
cwd = os.getcwd()

# Specify the correct path to the file
file_path = os.path.join(cwd, '/Users/ashim/Desktop/Professional course/pandas/ecommerce_sales_analysis.csv')

# Read the CSV file
df = pd.read_csv(file_path)

months= [f"sales_month_{i}" for i in range(1, 13)]
df['total_sales'] = df[months].sum(axis= 1)
category_sales = df.groupby('category')[months].sum()
fig, ax = plt.subplots()