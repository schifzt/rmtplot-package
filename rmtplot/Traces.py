# -*- coding: utf-8 -*-
#!bin/python3

import plotly.graph_objects as go


class Traces:
    def __init__(self, args):
        self.df_eigenvals = args['df_eigenvals']
        self.df_pdf = args['df_pdf']
        self.color = args['color']
        self.fill = args['fill']
        self.params = args['params']
        self.eigen_type = args['eigen_type']

        self.data = []

        self.spectral_density = []
        self.empirical_dist = []
        self.empirical_dist_rug = []

    def fit(self):
        if self.eigen_type == 'real':
            if self.df_pdf is not None:
                self._fit_spectral_density_real()
                self.data.extend(self.spectral_density)

            if self.df_eigenvals is not None:
                self._fit_empirical_dist_real()
                self._fit_empirical_dist_real_rug()

                self.data.extend(self.empirical_dist)
                self.data.extend(self.empirical_dist_rug)

        elif self.eigen_type == 'complex':
            if self.df_pdf is not None:
                self._fit_spectral_density_complex()
                self.data.extend(self.spectral_density)

            if self.df_eigenvals is not None:
                self._fit_empirical_dist_complex()
                self.data.extend(self.empirical_dist)

        return self

    def _fit_spectral_density_real(self):
        p_keys = list(self.params.keys())

        if not p_keys:  # if p_keys == []
            for _, df2 in self.df_pdf.groupby("group"):
                self.spectral_density.extend([
                    go.Scatter(
                        mode='lines',
                        x=df2['real_part'].values,
                        y=df2['density'].values,
                        name='spectral density',
                        line=dict(
                            color=self.color['line'],
                            dash='solid',
                            width=3
                        ),
                        showlegend=False,
                        visible=True,
                    )
                ])

            self.spectral_density[-1]['showlegend'] = True
        else:
            for p_valpair, df1 in self.df_pdf.groupby(p_keys):
                for _, df2 in df1.groupby("group"):
                    p_legend = ' '
                    for i, p_key in enumerate(p_keys):
                        if i > 0:
                            p_legend += ', '
                        p_legend += p_key + '=' + str(p_valpair[i])

                    self.spectral_density.extend([
                        go.Scatter(
                            mode='lines',
                            x=df2['real_part'].values,
                            y=df2['density'].values,
                            name='spectral density' + p_legend,
                            line=dict(
                                color=self.color['line'],
                                dash='solid',
                                width=3
                            ),
                            showlegend=False,
                            visible=True,
                        )
                    ])

                self.spectral_density[-1]['showlegend'] = True

        if self.fill:
            for scatter in self.spectral_density:
                scatter['fill'] = 'tonexty'
                scatter['fillcolor'] = self.color['fill']

        return self

    def _fit_empirical_dist_real(self):
        self.empirical_dist = [go.Histogram(
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
        )]

        return self

    def _fit_empirical_dist_real_rug(self):
        self.empirical_dist_rug = [go.Box(
            x=self.df_eigenvals['real_part'],
            name='',
            boxpoints='all', hoverinfo='x', hoveron='points', jitter=0, y0=0,
            marker=dict(
                symbol='line-ns-open',
                color=self.color['rug'],
                size=20,
            ),
            showlegend=False, fillcolor='rgba(255,255,255,0)', line_color='rgba(255,255,255,0)',
        )]

    def _fit_spectral_density_complex(self):
        for _, df in self.df_pdf.groupby("group"):
            self.spectral_density.extend([
                go.Scatter(
                    name='boundary of the support',
                    x=df['real_part'].values,
                    y=df['imag_part'].values,
                    line=dict(
                        color=self.color['line'],
                        dash='solid',
                        width=3
                    ),
                    showlegend=False
                )
            ])

        self.spectral_density[0]['showlegend'] = True

        if self.fill:
            for scatter in self.spectral_density:
                scatter['fill'] = 'tonexty'
                scatter['fillcolor'] = self.color['fill']

        return self

    def _fit_empirical_dist_complex(self):
        self.empirical_dist = [go.Scatter(
            name='sample',
            mode='markers',
            type='scatter',
            x=self.df_eigenvals['real_part'],
            y=self.df_eigenvals['imag_part'],
            marker=dict(
                color=self.color['border'],
                size=3
            )
        )]

        return self
