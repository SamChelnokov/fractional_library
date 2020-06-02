import python_llibrary as pl
import math

def f(x):
    return math.sin(x)

print("start")

c_value_norm = 0.45969769413186028260
c_value_frac = 0.46371687684454652288
print("Compare left reactangular fractional and normal formul for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 1")
for i in range(0, 7):
    print("n = ", pow(10, i))
    v_fr = pl.LeftFractionalRectangularFormul(0.99, 1, pow(10, i), f)
    print("Left fracional rectangular formul value =")
    print(v_fr)
    print(" ")
    print("Erorr Fractional = ")
    print(math.fabs(c_value_frac - v_fr))
    print(" ")
    print("Erorr Normal =")
    v = pl.LeftRectangularFormal(1, pow(10, i), f)
    print(math.fabs(c_value_norm - v))
    print("##############")
   
print("Compare right rectangular fractional and normal formul for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 1")
for i in range(0, 7):
    print("n = ", pow(10, i))
    v_fr = pl.RightFractionalRectangularFormul(0.99, 1, pow(10, i), f)
    print("Right fracional rectangular formul value =")
    print(v_fr)
    print(" ")
    print("Erorr Fractional = ")
    print(math.fabs(c_value_frac - v_fr))
    print(" ")
    print("Left rectangular formul value =")
    v = pl.RightRectangularFormal(1, pow(10, i), f)
    print(v)
    print(" ")
    print("Erorr Normal =")
    print(math.fabs(c_value_norm - v))
    print("##############")

print("Compare trapezoidal fractional and normal formul for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 1")
for i in range(0, 7):
    print("n = ", pow(10, i))
    v_fr = pl.FractionalTrapezoidalFormul(0.99, 1, pow(10, i), f)
    print("Trapezoidal fractional formul value =")
    print(v_fr)
    print(" ")
    print("Erorr Fractional = ")
    print(math.fabs(c_value_frac - v_fr))
    print(" ")
    v = pl.TrapezoidalFormul(1, pow(10, i), f)
    print("Trapezoidal fractional formul value =")
    print(v)
    print(" ")
    print("Erorr Normal =")
    print(math.fabs(c_value_norm - v))
    print("##############")

print("Compare Simpsons fractional and normal formul for function sin(x) with intervals(n) and integrate from 0 to 1 with alpha = 1")
for i in range(0, 7):
    print("n = ", pow(10, i))
    v_fr = pl.FractionalSimpsonSFormul(0.99, 1, pow(10, i), f)
    print("Simpsons Fractional formul value =")
    print(v_fr)
    print(" ")
    print("Erorr Fractional = ")
    print(math.fabs(c_value_frac - v_fr))
    print(" ")
    v = pl.SimpsonsFormul(1, pow(10, i), f)
    print("Simpsons formul value =")
    print(v)
    print(" ")
    print("Erorr Normal =")
    print(math.fabs(c_value_norm - v))
    print("##############")