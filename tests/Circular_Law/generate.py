#!/usr/bin/env python3

import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


n = 1000

params = np.array([n])
np.savetxt('params.csv', params, delimiter=',', fmt='%.3f')

# Generate a random matrix
# X: n x n matrices

mean = np.zeros(n)
cov = np.identity(n) / n
X = np.random.multivariate_normal(mean, cov, n)

eigenvals = np.linalg.eigvals(X)

# eigenvals must be 2 x n array
eigenvals = np.array([eigenvals.real, eigenvals.imag])

np.savetxt('eigenvals.csv', eigenvals, delimiter=',', fmt='%.3f')


# Generate p.d.f. points

step = 0.025
x = np.arange(-2.0, 2.0, step)
y = np.arange(-2.0, 2.0, step)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

fig, ax = plt.subplots()
cs = ax.contour(x, y, z, [1])

p = cs.collections[0].get_paths()[0]
v = p.vertices
x = v[:, 0]
y = v[:, 1]

points = np.array([x, y])

np.savetxt('support_boundary.csv', points, delimiter=',', fmt='%.3f')
