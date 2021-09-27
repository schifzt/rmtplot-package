# -*- coding: utf-8 -*-
#!bin/python3

import plotly.graph_objects as go
from rmtplot.Traces import Traces
import numpy as np
# import importlib


class RMTplot:
    def __init__(
            self,
            df_eigenvals,
            df_pdf,
            *,
            color='lavender',
            theme='matlab',
            fill=False,
            gridline=False,
            save_img_as='png'
    ):
        self.df_eigenvals = df_eigenvals
        self.df_pdf = df_pdf
        self.color = color
        self.theme = theme
        self.fill = fill
        self.gridline = gridline
        self.save_img_as = save_img_as

        self.check_eigen_type()

    def check_eigen_type(self):
        if np.count_nonzero(self.df_eigenvals['imag_part'].values) == 0:
            self.eigen_type = 'real'
        else:
            self.eigen_type = 'complex'

    def get_components(self):
        return self._create_traces(), self._create_layout(), self._create_config()

    def _create_traces(self):
        traces = Traces(
            args=vars(self)
        )

        traces.fit()

        return traces

    def _create_config(self):
        config = dict(
            responsive=True,
            showSendToCloud=False,
            plotlyServerURL="https://chart-studio.plotly.com",
            toImageButtonOptions=dict(
                format=self.save_img_as,
                filename='rmt',
                # height=600,
                # width=600,
                scale=2
            ),
            displayModeBar=True,
            displaylogo=False,
            modeBarButtonsToRemove=[
                'zoomIn2d',
                'zoomOut2d',
                'select2d',
                'lasso2d',
                'autoScale2d',
                'refitScale2d',
                'sendDataToCloud',
                'hoverClosestCartesian',
                'hoverCompareCartesian'
            ]
        )

        if self.theme == 'icon':
            config['scrollZoom'] = False
            config['staticPlot'] = True
        else:
            config['scrollZoom'] = True
            config['staticPlot'] = False

        return config

    def _create_layout(self):
        if self.theme == 'icon':
            return (
                go.Layout(
                    dragmode=False,
                    hovermode=False,
                    xaxis=dict(
                        showgrid=False, showline=False, showticklabels=False
                    ),
                    yaxis=dict(
                        showgrid=False, showline=False, showticklabels=False
                    ),
                    paper_bgcolor='rgba(255, 255, 255, 0)',
                    plot_bgcolor='rgba(255, 255, 255, 0)',
                    margin=dict(
                        t=0,
                        b=0,
                        l=0,
                        r=0,
                    ),
                    boxgap=1, boxgroupgap=1,
                )
            )

        layout = go.Layout(
            dragmode='pan',
            hovermode='closest',
            xaxis=dict(
                showgrid=False,
                showline=True, linewidth=2, linecolor='rgba(0, 0, 0, 1)',
                showticklabels=True, ticks='inside',
                autorange=True, rangemode='normal',
                automargin=False,

            ),
            yaxis=dict(
                showgrid=False,
                showline=True, linewidth=2, linecolor='rgba(0, 0, 0, 1)',
                showticklabels=True, ticks='inside',
                autorange=True, rangemode='normal',
                automargin=False,
            ),
            paper_bgcolor='rgba(255, 255, 255, 0)',
            plot_bgcolor='rgba(255, 255, 255, 0)',
            legend=dict(
                x=1, xanchor='right',
                y=1,
                bgcolor='rgba(255, 255, 255, 0.65)'
            ),
            modebar=dict(
                orientation='h'
            ),
            margin=dict(
                autoexpand=False,
                pad=0,
                t=30,  # Fix
                r=20,  # Fix
                b=45,  # Shift the same amount with l
                l=55,  # Shift the same amount with b
            ),
            boxgap=1, boxgroupgap=1,
        )

        if self.theme == 'matlab':
            layout.update(
                dict(
                    xaxis=dict(
                        mirror='all',
                    ),
                    yaxis=dict(
                        mirror='all',
                    )
                )
            )
        elif self.theme == 'classic':
            layout.update(
                dict(
                    xaxis=dict(
                        mirror=False,
                    ),
                    yaxis=dict(
                        mirror=False,
                    )
                )
            )

        if self.gridline:
            layout.update(
                xaxis=dict(
                    showgrid=True, gridwidth=1, gridcolor='rgba(238, 238, 238, 1)',
                    zeroline=True, zerolinewidth=1, zerolinecolor='rgba(0, 0, 0, 1)',
                ),
                yaxis=dict(
                    showgrid=True, gridwidth=1, gridcolor='rgba(238, 238, 238, 1)',
                    zeroline=True, zerolinewidth=1, zerolinecolor='rgba(0, 0, 0, 1)',
                )
            )

        if self.eigen_type == 'real':
            layout.update(
                yaxis=dict(
                    rangemode='nonnegative'
                ),
                xaxis_title=r'$\lambda$',
                yaxis_title=r'$\rho(\lambda)$',
                font=dict(
                    size=16,
                )
            )
        elif self.eigen_type == 'complex':
            layout.update(
                xaxis_title=r'$\text{Re}\,\lambda$',
                yaxis_title=r'$\text{Im}\,\lambda$',
                font=dict(
                    size=16,
                )
            )

        return layout
