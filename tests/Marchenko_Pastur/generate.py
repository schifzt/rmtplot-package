#!/usr/bin/env python3

import numpy as np
import pandas as pd

a = 0.2    # d/n
n = 1000
d = int(n*a)

params = np.array([a, n, d])
np.savetxt('params.csv', params, delimiter=',', fmt='%.3f')

# Generate a random matrix
# X: d x n matrices
# Y: n x n matrices

mean = np.zeros(n)
cov = np.identity(n)
X = np.random.multivariate_normal(mean, cov, d)
Y = X@X.T / n

eigenvals = np.linalg.eigvals(Y)

df_eigenvals = pd.DataFrame(data={
    'real_part': eigenvals.real,
    'imag_part': eigenvals.imag
})

df_eigenvals.to_csv('eigenvals.csv', index=False, encoding='utf-8')


# Generate p.d.f. points
def density(x, y, a):
    lb = (1-np.sqrt(a))**2
    ub = (1+np.sqrt(a))**2

    if 1 <= a and x == 0:
        return 1 - 1/a

    if lb <= x and x <= ub:
        return 1 / (2 * np.pi * x * a) * np.sqrt((ub - x) * (x - lb))
    else:
        return 0


domain = [0, np.max(eigenvals).real + 1]
step = 0.01
n = int(domain[1] - domain[0]) / step

x = np.arange(domain[0], domain[1], step)
d = np.frompyfunc(density, 3, 1)(x, y, a)

df_pdf = pd.DataFrame(data={
    'real_part': x,
    'imag_part': 0,
    'density': d
})

df_pdf.to_csv('pdf.csv', index=False, encoding='utf-8')
