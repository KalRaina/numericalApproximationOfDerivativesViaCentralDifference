# numericalApproximationOfDerivativesViaCentralDifference
Approximating derivatives of curve f(x) = x**4 + 3*(x**3) + 2 via central difference method.

# DESCRIPTION

This project calculates the derivative of  f(x) = x^4 + 3x^3 + 2 at specific poitns based on user input, using the central difference method with decreasing step size h.

## HOW IT WORKS

We approximate the derivative using the central difference quotient:

    f'(x) ≈ (f(x + h) - f(x - h)) / (2h)

The step size h is reduced by one of order magnitude every iteration to improve accuracy, and unstable estimates are filtered out within the for loop.

## FINAL RESULTS

Numerical estimate of f'(x) at a specific x-coordinate and plot of the function and tangent line on the Cartesian Plane


