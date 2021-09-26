#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.cm as cm
import matplotlib.pyplot as plt

'''
Implementation of this paper:
    title: Location of the spectrum of Kronecker random matrices
    authors: Johannes Alt, László Erdős, Torben Krüger, Yuriy Nemish
    DOI: 10.1214/18-AIHP894
'''


# params = np.array([n])
# np.savetxt('params.csv', params, delimiter=',', fmt='%.3f')

'''
Generate a random matrix
    a: L x L matrices
    I: N x N identity matrices
    W: NL x NL matrices
    X: NL x NL matrices
'''

N = 5000

pole = [-0.97, 0.97]
# pole = [-1.0, 1.0]
# pole = [-1.03, 1.03]
# pole = [0, -1.4, 1.4, 0.8+1.26j, -0.8+1.26j]
# pole = [complex(np.cos(pm1*np.pi/6), np.sin(pm1*np.pi/6))*(pm2*0.97)
#         for pm1 in [+1, -1] for pm2 in [+1, -1]]


a = np.diagflat(pole)
I = np.identity(N)

L = a.shape[0]

mean = np.zeros(N*L)
cov = np.identity(N*L) / (N*L)
W = np.random.multivariate_normal(mean, cov, N*L)

X = np.kron(I, a) + W

eigenvals = np.linalg.eigvals(X)

df_eigenvals = pd.DataFrame(data={
    'real_part': eigenvals.real,
    'imag_part': eigenvals.imag
})

df_eigenvals.to_csv(str(Path(__file__).resolve().parent) + '/eigenvals.csv',
                    index=False, encoding='utf-8')


'''
Generate density function points
    See equation (2.15) in the paper
'''

step = 0.025
re, im = np.meshgrid(np.arange(-3.0, 3.0, step), np.arange(-3.0, 3.0, step))
w = re + im*1j

z = np.sum([np.divide(1, abs(w - pole[l])**2) for l in range(L)], axis=0)
# z[np.isinf(z)] = 10000

fig, ax = plt.subplots()
cs = ax.contour(re, im, z, [L])
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
              index=False, encoding='utf-8')
