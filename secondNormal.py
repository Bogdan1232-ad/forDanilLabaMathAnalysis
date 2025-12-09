import numpy as np
import matplotlib.pyplot as plt

def logistic(x, r):
    return r * x * (1 - x)

def logistic_list(x_0, r, steps):
    xs = [x_0]
    for i in range(steps):
        x_next = logistic(xs[-1], r)
        xs.append(x_next)
    return np.array(xs)

r = 0.9
x_0 = 0.9
steps = 100

xs = logistic_list(x_0, r, steps)

plt.figure(figsize=(8, 8))
plt.plot(range(steps + 1), xs, marker='o', linestyle='', color = 'darkblue')
plt.title(f'Logistic Map: r={r}, x_0={x_0}')
plt.xlabel('n')
plt.ylabel('x_n')
plt.grid(True)
plt.savefig('secondNormal.pdf')

plt.show()


