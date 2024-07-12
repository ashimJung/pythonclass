import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()
li=[random.randint(1,50) for _ in range(4)]
def animate(i):
  ax.clear()
  li = [random.randint(1,50) for _ in range(4)]
  ax.bar([1,2,3,4],li)
  ax.set_xlabel("x-axis")
  ax.set_ylabel("y-axis")
  ax.set_title("Animate")
ani = animation.FuncAnimation(fig, animate, frames=100, interval = 1000, blit = False )
plt.show()