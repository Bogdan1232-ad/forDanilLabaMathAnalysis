import numpy as np
import matplotlib.pyplot as plt 
import sympy as sp

def g(x, r):
    return r * x * (1 - x) * (3 - x)

def list_g(x_0, r, steps):
    xs = [x_0]
    x = x_0
    for i in range(steps):
        x = g(x, r)
        xs.append(x)
    return np.array(xs)

def detect_per(xs_last, max_period=64, tol=1e-6):
    k = len(xs_last)
    for i in range(1, max_period + 1):
        is_periodic = True
        for j in range(k - i):
            if abs(xs_last[j] - xs_last[j + i]) > tol:
                is_periodic = False
                break
        if is_periodic:
            return i
    return None

def study_periods(r_min=0.0, r_max=1.58, num_r=300, x_0 = 0.2, total_steps=2000, tail_len = 200, max_period = 64):
    rs = np.linspace(r_min, r_max, num_r)
    periods = []

    for r in rs:
        xs = list_g(x_0, r, total_steps)
        xs_tail = xs[-tail_len:]
        period = detect_per(xs_tail, max_period=max_period)
        if period is None:
            periods.append(0)
        else:
            periods.append(period)
        
    periods = np.array(periods)

    plt.figure(figsize=(7, 7))
    plt.plot(rs, periods, marker='.', color='darkblue', markersize=3)
    plt.title('Длина цикла')
    plt.xlabel('r')
    plt.ylabel('Период цикла')
    plt.grid(True)
    plt.savefig('fourthhard.pdf')
    plt.show()

    return rs, periods

rs, periods = study_periods()