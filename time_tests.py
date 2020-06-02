import python_llibrary as pl
import timeit
import math

def f(x):
    return math.sin(x)


print("start")
print("Caputo Trapezoidal Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    def func():
        return pl.Caputo_0FractionalTrapezoidalFormul(0.5, 1, 1, n, f)

    t = timeit.timeit(func, number=100)/100
    print('n = {0}, time = {1}'.format(n, t))

print(" ")

print("Left Caputo Rectangular Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    def func():
        return pl.LeftCaputo_0FractionalRectangularFormul(0.5, 1, n, f)

    t = timeit.timeit(func, number=100)/100
    print('n = {0}, time = {1}'.format(n, t))

print(" ")

print("Right Caputo Rectangular Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    def func():
        return pl.RightCaputo_0FractionalRectangularFormul(0.5, 1, n, f)

    t = timeit.timeit(func, number=100)/100
    print('n = {0}, time = {1}'.format(n, t))

print(" ")

print("Fractional Simpsons Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    def func():
        return pl.FractionalSimpsonSFormul(0.5, 1, n, f)

    t = timeit.timeit(func, number=100)/100
    print('n = {0}, time = {1}'.format(n, t))

print(" ")

print("Fractional Trapezoidal Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    def func():
        return pl.FractionalTrapezoidalFormul(0.5, 1, n, f)

    t = timeit.timeit(func, number=100)/100
    print('n = {0}, time = {1}'.format(n, t))

print(" ")

print("Left fractional rectangular Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    def func():
        return pl.LeftRectangularFormal(0.5, 1, n, f)

    t = timeit.timeit(func, number=100)/100
    print('n = {0}, time = {1}'.format(n, t))

print(" ")

print("Right fractional rectangular Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for n in (1, 10, 100, 1000, 10000, 100000, 1000000):
    def func():
        return pl.RightRectangularFormal(0.5, 1, n, f)

    t = timeit.timeit(func, number=100)/100
    print('n = {0}, time = {1}'.format(n, t))
