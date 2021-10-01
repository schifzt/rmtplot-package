#!/usr/bin/env python3

import itertools
import numpy as np
import pandas as pd
from pathlib import Path
from collections import OrderedDict

params = dict(
    a=[0.2, 0.4, 0.6, 0.8],  # d/n
    b=[1]
)

n = 1000
d = [int(n*a) for a in params['a']]

# params = pd.DataFrame(data={'a': a, 'n': n, 'd': d}, index=[0])
# params.to_csv(str(Path(__file__).resolve().parent) + '/parameters.csv',
#               encoding='utf-8', float_format='%.4f')


'''
Generate a random matrix
    X: d x n matrices
    Y: n x n matrices
'''

mean = np.zeros(n)
cov = np.identity(n)
X = np.random.multivariate_normal(mean, cov, d[0])
Y = X@X.T / n

eigenvals = np.linalg.eigvals(Y)

df_eigenvals = pd.DataFrame(data={
    'real_part': eigenvals.real,
    'imag_part': eigenvals.imag
})

df_eigenvals.to_csv(str(Path(__file__).resolve().parent) + '/eigenvals.csv',
                    index=False, encoding='utf-8', float_format='%.4f')


'''
Generate density function points
'''


def density(x, a, b):
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


df_pdf = pd.DataFrame(
    columns=list(params.keys()) + ['real_part', 'imag_part', 'density', 'group'])

p_keys = list(params.keys())
for p_vals in itertools.product(*params.values()):
    x = np.arange(domain[0], domain[1], step)
    d = np.array([density(x, *p_vals) for x in x])

    vs = [np.hstack((x.reshape(-1, 1), d.reshape(-1, 1)))]

    for i, v in enumerate(vs):
        df = pd.DataFrame(data={**OrderedDict(zip(p_keys, p_vals)), **OrderedDict({
            'real_part': v[:, 0],
            'imag_part': 0,
            'density': v[:, 1],
            'group': i
        })})

        df_pdf = pd.concat([df_pdf, df], ignore_index=True)


df_pdf.to_csv(str(Path(__file__).parent) + '/pdf.csv',
              index=False, encoding='utf-8', float_format='%.4f')
