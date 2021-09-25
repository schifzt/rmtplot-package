# -*- coding: utf-8 -*-
#!bin/python3

import plotly.graph_objects as go


class Traces:
    def __init__(self, args):
        self.df_eigenvals = args['df_eigenvals']
        self.df_pdf = args['df_pdf']
        self.color = args['color']
        self.fill = args['fill']
        self.eigen_type = args['eigen_type']

        self.empirical_dist = dict()
        self.empirical_dist_rug = dict()
        self.spectral_density = dict()

    def fit(self):
        if self.eigen_type == 'real':
            self._fit_empirical_dist_real()
            self._fit_spectral_density_real()
            self._fit_empirical_dist_real_rug()
        elif self.eigen_type == 'complex':
            self._fit_empirical_dist_complex()
            self._fit_spectral_density_complex()

        return self

    def _fit_empirical_dist_real(self):
        self.empirical_dist = go.Histogram(
            x=self.df_eigenvals['real_part'],
            histnorm='probability density',
            name='empirical distribution',
            marker=dict(
                color=self.color['fill'],
                line=dict(
                    color=self.color['border'],
                    width=2,
                ),
                pattern=dict(
                    fillmode='overlay',
                )
            ),
            xbins=dict(
                size=0.05
            ),
            hoverinfo='skip',
        )

        return self

    def _fit_empirical_dist_real_rug(self):
        self.empirical_dist_rug = go.Box(
            x=self.df_eigenvals['real_part'],
            name='',
            boxpoints='all', hoverinfo='x', hoveron='points', jitter=0,
            marker=dict(
                symbol='line-ns-open',
                color=self.color['rug'],
                size=20,
            ),
            showlegend=False, fillcolor='rgba(255,255,255,1)', line_color='rgba(255,255,255,0)',
        )

    def _fit_spectral_density_real(self):
        self.spectral_density = go.Scatter(
            mode='lines',
            x=self.df_pdf['real_part'],
            y=self.df_pdf['density'],
            name='spectral density',
            line=dict(
                color=self.color['line'],
                dash='solid',
                width=3
            )
        )

        if self.fill:
            self.spectral_density['fill'] = 'tonexty'
            self.spectral_density['fillcolor'] = self.color['fill']

        return self

    def _fit_empirical_dist_complex(self):
        self.empirical_dist = go.Scatter(
            name='sample',
            mode='markers',
            type='scatter',
            x=self.df_eigenvals['real_part'],
            y=self.df_eigenvals['imag_part'],
            marker=dict(
                color=self.color['border'],
                size=3
            )
        )

        return self

    def _fit_spectral_density_complex(self):
        self.spectral_density = go.Scatter(
            name='boundary of the support',
            x=self.df_pdf['real_part'],
            y=self.df_pdf['imag_part'],
            line=dict(
                color=self.color['line'],
                dash='solid',
                width=3
            )
        )

        if self.fill:
            self.spectral_density_bd['fill'] = 'tonexty'
            self.spectral_density_bd['fillcolor'] = self.color['fill']

        return self
