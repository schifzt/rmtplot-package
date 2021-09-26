#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt


n = 5000

params = np.array([n])
np.savetxt('params.csv', params, delimiter=',', fmt='%.3f')

# Generate a random matrix
# X: n x n matrices

mean = np.zeros(n)
cov = np.identity(n) / n
X = np.random.multivariate_normal(mean, cov, n)

eigenvals = np.linalg.eigvals(X)

df_eigenvals = pd.DataFrame(data={
    'real_part': eigenvals.real,
    'imag_part': eigenvals.imag
})

df_eigenvals.to_csv('eigenvals.csv', index=False, encoding='utf-8')


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

df_pdf = pd.DataFrame(data={
    'real_part': x,
    'imag_part': y,
    'density': None
})

df_pdf.to_csv('pdf.csv', index=False, encoding='utf-8')
