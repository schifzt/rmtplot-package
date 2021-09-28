#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.cm as cm
import matplotlib.pyplot as plt


n = 5000

params = np.array([n])
np.savetxt(str(Path(__file__).resolve().parent) + '/parameters.csv', params,
           delimiter=',', fmt='%.4f')

'''
Generate a random matrix
    X: n x n matrices
'''

mean = np.zeros(n)
cov = np.identity(n) / n
X = np.random.multivariate_normal(mean, cov, n)

eigenvals = np.linalg.eigvals(X)

df_eigenvals = pd.DataFrame(data={
    'real_part': eigenvals.real,
    'imag_part': eigenvals.imag
})

df_eigenvals.to_csv(str(Path(__file__).resolve().parent) + '/eigenvals.csv',
                    index=False, encoding='utf-8', float_format='%.4f')


# Generate p.d.f. points

step = 0.01
re, im = np.meshgrid(np.arange(-2.0, 2.0, step), np.arange(-2.0, 2.0, step))
z = re**2 + im**2

fig, ax = plt.subplots()
cs = ax.contour(re, im, z, [1])
p = cs.collections[0].get_paths()
vs = [p_.vertices for p_ in p]

df_pdf = pd.DataFrame(columns=['real_part', 'imag_part', 'density', 'group'])

for i, v in enumerate(vs):
    df = pd.DataFrame(data={
        'real_part': v[:, 0],
        'imag_part': v[:, 1],
        'density': None,
        'group': i
    })

    df_pdf = pd.concat([df_pdf, df], ignore_index=True)


df_pdf.to_csv(str(Path(__file__).parent) + '/pdf.csv',
              index=False, encoding='utf-8', float_format='%.4f')
