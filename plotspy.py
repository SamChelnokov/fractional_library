import numpy as np
from matplotlib import pyplot as plt
import python_llibrary as pl


def f(x):
    return np.sin(x)

alpha_arr = np.array([0, 0.25, 0.5, 0.75, 1.0])
for a in alpha_arr:
    x = np.arange(0, 12, 0.1)
    y = np.array([pl.Caputo_0FractionalTrapezoidalFormul(a, 1, t, 1000, f) for t in x])
    plt.plot(x, y, label='a={0}'.format(a))
    
plt.legend()
plt.show()
plt.savefig('plot_trapezoidal.pdf')

import timeit

for n in (10, 100, 1000, 10000):
    def func():
        return pl.Caputo_0FractionalTrapezoidalFormul(a, 1, 1, n, f)

    t = timeit.timeit(func, number=100) / 100.
    print('n = {0}, time = {1}'.format(n, t))


print("Fractional right 0 Caputo Rectangular Formula for function sin(x) with intervals(n) and derivates from 0 to 1 with alpha = 0.5")
nvars = []
values = []
for i in range(1, 7):
    n = 10**i
    nvars.append(n)
    v = pl.RightCaputo_0FractionalRectangularFormul(0.5, 1, pow(10, i), f)
    values.append(v)
    print("n = ", pow(10, i))
    print(v)

nvars = np.array(nvars)
values = np.array(values)
errors = np.abs(value_exact - values)
plt.plot(nvars, errors, label='Caputo Rectangular')

plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.show()
plt.savefig('plot.pdf')