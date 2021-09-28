#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.cm as cm
import matplotlib.pyplot as plt


N = 2000

params = np.array([N])
np.savetxt(str(Path(__file__).resolve().parent) + '/parameters.csv', params,
           delimiter=',', fmt='%.4f')

'''
Generate a Gaussian Orthogonal Ensemble(GOE)
X: N x N matrices
    X_ij: N(0,4)
M: N x N symmetric matrices
    M_ij: N(0,1)
    M_ii: N(0,2)
'''

mean = np.zeros(N)
cov = np.identity(N)*2
X = np.random.multivariate_normal(mean, cov, N)
M = (X + X.T)/2
Y = M / np.sqrt(N)

eigenvals = np.linalg.eigvals(Y)

df_eigenvals = pd.DataFrame(data={
    'real_part': eigenvals.real,
    'imag_part': eigenvals.imag
})

df_eigenvals.to_csv(str(Path(__file__).resolve().parent) + '/eigenvals.csv',
                    index=False, encoding='utf-8', float_format='%.4f')


'''
Generate p.d.f. points
    y = 1/(2*pi)*np.sqrt(4-x**2)
'''

step = 0.01
x, y = np.meshgrid(np.arange(-3.0, 3.0, step), np.arange(0.0, 1.0, step))
z = x**2 + (2*np.pi*y)**2

fig, ax = plt.subplots()
cs = ax.contour(x, y, z, [4])
p = cs.collections[0].get_paths()
vs = [p_.vertices for p_ in p]

df_pdf = pd.DataFrame(columns=['real_part', 'imag_part', 'density', 'group'])

for i, v in enumerate(vs):
    df = pd.DataFrame(data={
        'real_part': v[:, 0],
        'imag_part': 0,
        'density': v[:, 1],
        'group': i
    })

    df_pdf = pd.concat([df_pdf, df], ignore_index=True)


df_pdf.to_csv(str(Path(__file__).parent) + '/pdf.csv',
              index=False, encoding='utf-8', float_format='%.4f')
