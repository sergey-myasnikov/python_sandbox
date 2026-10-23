"""
Euler's Identity (Complex Analysis)

The famous formula e^i*pi + 1 = 0 connects the five main mathematical constants.
It implies that e = (-1)^-1/i*pi, but it is easier to use the formula via complex sine and cosine:
e = cos(-i) + i*sin(-i).

In Python, the built-in support for complex numbers allows to do this in a single line.
"""

import cmath

# Get e via the exponential of the complex number 1j (the imaginary unit)
e_complex = cmath.exp(1)

# Output the real part
print(e_complex.real)