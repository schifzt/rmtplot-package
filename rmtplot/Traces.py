# -*- coding: utf-8 -*-
#!bin/python3

import plotly.graph_objects as go

"""
TODO:
Detect a type(real or complex) by looking for eigenvals, and fit() depends on this type.
"""


class Traces:
    def __init__(self, df_eigenvals, df_pdf, color, fill):
        self.df_eigenvals = df_eigenvals
        self.df_pdf = df_pdf
        self.color = color
        self.fill = fill

    def fit(self):
        # if real
        self._fit_histogram1d()
        self._fit_density1d()

        # if complex

        return self

    def _fit_histogram1d(self):
        self.histogram1d = go.Histogram(
            x=self.df_eigenvals['real_part'],
            histnorm='probability density',
            name='empirical',
            marker=dict(
                color=self.color['fill'],
                line=dict(
                    color=self.color['fill'],
                    width=2
                ),
                pattern=dict(
                    fillmode='overlay'
                )
            ),
            opacity=1.0,
            xbins=dict(
                size=0.05
            ),
            hoverinfo='skip'
        )

        return None

    def _fit_density1d(self):
        self.density1d = go.Scatter(
            mode='lines',
            x=self.df_pdf['real_part'],
            y=self.df_pdf['density'],
            name='p.d.f.',
            line=dict(
                color=self.color['line'],
                dash='solid',
                width=2
            )
        )

        if self.fill:
            self.density1d['fill'] = 'tonexty'
            self.density1d['fillcolor'] = self.color['fill']

        return None
