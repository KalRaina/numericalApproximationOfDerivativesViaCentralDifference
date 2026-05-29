import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + 3*(x**3) + 2 # curve

point = float(input("Give the x coordinate of the point where you wish to find the gradient of the function x**4 + 3*(x**3) + 2: "))

x = np.linspace(point-50, point+50,4000)
h = 1e-3 

list = []
derivs = []

for i in range(4):
   
   idk = (-f(point+2*h) + 8*f(point+h) - 8*f(point-h) + f(point-2*h)) / (12*h) # central difference derivative
   

   if len(derivs) == 0:
       derivs.append(idk)
   else:
       if abs(idk-derivs[-1]) < 0.5: # stability filtering, for reference, [-1] means last element
           derivs.append(idk)

derivs = np.array(derivs)
estimate = derivs.mean()
print(estimate)

m = estimate
c = f(point) - m * point

smth = np.linspace(point-50, point+50,4000)
y2 = m * smth + c # slope intercept form of tangent line

plt.plot(smth, y2, color = "red", label = "Tangent Line") # plot tangent line
plt.plot(x, f(x), label = "Curve") # plot curve

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.axhline(0, color="black", linewidth=1)   # x-axis
plt.axvline(0, color="black", linewidth=1)   # y-axis

plt.grid(True)
plt.show()