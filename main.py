import matplotlib.pyplot as plt

def get_next(r, x_n):
    return r*x_n*(1-x_n)

x, y =[], [] 

# Initial Condition
x_n = 0.5
# Growth Rate
r = 3

for i in range(1,100):
    x.append(i)
    x_n = get_next(r, x_n)
    y.append(x_n)

plt.scatter(x, y, c ="black", s = 1)
  
# To show the plot
plt.show()