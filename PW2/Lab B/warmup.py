"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
x0=0 
lr=0.1
x=x0 
while (True):
    step=lr*df(x)
    x=x-step 
    if abs(step)<0.000001:
        break
print("Gradient descent:", x)

#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
x_new=newton(df, x0, fprime=d2f)
print("Newton:", x_new)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")
x_min=minimize(f, x0, method="SLSQP")
print("SLSQP:", x_min)
# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?
for x0 in [0.0,2.0]:
    x=x0
    lr=0.01
    while True:
        step=lr*dg(x)
        x=x-step 
        if abs(step)<0.000001:
            break 
    print("Gradient descent:", x) 
    x_new=newton(dg, x0, fprime=d2g) 
    sec_der=d2g(x_new) 
    print("g at Newton ",sec_der)
    if (sec_der<0):
        print("Newton found maximum")
    if (sec_der>0):
        print("Newton found minimum")
    x_min=minimize(g, x0, method="SLSQP")
    print ("SLSQP: ",x_min)
