import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + 3*(x**3) + 2 # curve

point = float(input("Give the x coordinate of the point where you wish to find the gradient of the function x**4 + 3*(x**3) + 2: "))

x = np.linspace(-10,10,4000)
h = 0.1

list = []
derivs = []

for i in range(4):
   
   idk = (f(point+h) - f(point-h))/(2*h) # central difference derivative
   

   if len(derivs) == 0:
       derivs.append(idk)
   else:
       if abs(idk-derivs[-1]) < 0.5: # stability filtering, for reference, [-1] means last element
           derivs.append(idk)
   h = h/10

derivs = np.array(derivs)
estimate = derivs.mean()
print(estimate)

m = estimate
c = f(point) - m * point

smth = np.linspace(-20, 20, 400)
y2 = m * smth + c # slope intercept form of tangent line

plt.plot(smth, y2, color = "red") # plot tangent line
plt.plot(x, f(x)) # plot curve

plt.xlabel("x")
plt.ylabel("y")

plt.axhline(0, color="black", linewidth=1)   # x-axis
plt.axvline(0, color="black", linewidth=1)   # y-axis

plt.grid(True)
plt.show()