#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt


n = 2000

params = np.array([n])
np.savetxt('params.csv', params, delimiter=',', fmt='%.3f')

# Generate a Gaussian Orthogonal Ensemble(GOE)
# X: n x n matrices
#     X_ij: N(0,4)
# M: n x n symmetric matrices
#     M_ij: N(0,1)
#     M_ii: N(0,2)

mean = np.zeros(n)
cov = np.identity(n)*2
X = np.random.multivariate_normal(mean, cov, n)
M = (X + X.T)/2
Y = M / np.sqrt(n)

eigenvals = np.linalg.eigvals(Y)

df_eigenvals = pd.DataFrame(data={
    'real_part': eigenvals.real,
    'imag_part': eigenvals.imag
})

df_eigenvals.to_csv('eigenvals.csv', index=False, encoding='utf-8')


# Generate p.d.f. points
#     y = 1/(2*pi)*np.sqrt(4-x**2)

step = 0.025
x = np.arange(-3.0, 3.0, step)
y = np.arange(0.0, 1.0, step)
x, y = np.meshgrid(x, y)
z = x**2 + (2*np.pi*y)**2

fig, ax = plt.subplots()
cs = ax.contour(x, y, z, [4])

p = cs.collections[0].get_paths()[0]
v = p.vertices

x = v[:, 0]
d = v[:, 1]

df_pdf = pd.DataFrame(data={
    'real_part': x,
    'imag_part': 0,
    'density': d
})

df_pdf.to_csv('pdf.csv', index=False, encoding='utf-8')
