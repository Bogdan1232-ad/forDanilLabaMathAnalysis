import numpy as np
import matplotlib.pyplot as plt

def logistic(x, r):
    return r * x * (1 - x)

def lemerey(r, x_0 = 0.5, steps = 100):
    x_vals = np.linspace(0, 1, 400)
    y_vals = logistic(x_vals, r)

    plt.figure(figsize=(7, 7))


    xs = [x_0]
    plt.plot(x_vals, y_vals, label='f(x) = rx(1 - x)', color='darkblue')
    plt.plot(x_vals, x_vals, label='y = x', color='darkorange')
    plt.title(f'Lemerey')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    x = x_0
    for i in range(steps):
        y = logistic(x, r)
        xs.append(y)
        plt.plot([x, x], [x, y], color='darkgreen')
        plt.plot([x, y], [y, y], color='darkgreen')
        x = y
    plt.savefig('thirdhard3.9.pdf')
    plt.show()
    print(xs[-8:])


lemerey(r=3.9, x_0=0.2) 