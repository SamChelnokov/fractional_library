import python_llibrary as pl
import math

def f(x):
    return math.sin(x)
print("start")

def g(x):
    return 1

correct_value = 0.84605678672415297
print("Left Caputo Rectangular Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for i in range(0, 7):
    print("n = ", pow(10, i))
    v = pl.LeftCaputo_0FractionalRectangularFormul(0.5, 1, pow(10, i), f)
    ### print(v)
    print("Poryadok tochnosti =", (1/pow(10, i)))
    print("Erorr = ", math.fabs(v - correct_value) )
    print(" ")
    print("###############")

print("Right Caputo Rectangular Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for i in range(0, 7):
    print("n = ", pow(10, i))
    v = pl.RightCaputo_0FractionalRectangularFormul(0.5, 1, pow(10, i), f)
    print("Poryadok tochnosti =", (1/pow(10, i)))
    print("Erorr = ", math.fabs(v - correct_value))
    print(" ")
    print("###############")

print("Caputo Trapezoidal Formula for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 0.5")
for i in range(0, 7):
    print("n = ", pow(10, i))
    v = pl.Caputo_0FractionalTrapezoidalFormul(0.5, 1, 1, pow(10, i), f)
    print("Poryadok tochnosti =", (pow(1/pow(10, i), 2)))
    print("Erorr = ", math.fabs(v - correct_value))
    print(" ")
    print("###############")
