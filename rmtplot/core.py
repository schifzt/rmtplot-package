# -*- coding: utf-8 -*-
#!bin/python3

from rmtplot.Traces import Traces
from collections import OrderedDict
from itertools import product
import plotly.graph_objects as go
import numpy as np
# import importlib


class RMTplot:
    def __init__(
            self,
            *,
            df_eigenvals=None,
            df_pdf=None,
            color='lavender',
            theme='matlab',
            fill=False,
            slider=False,
            save_img_as='png'
    ):
        self.df_eigenvals = df_eigenvals
        self.df_pdf = df_pdf
        self.color = color
        self.theme = theme
        self.fill = fill
        self.slider = slider
        self.save_img_as = save_img_as

        self.validate_arguments()
        self.check_eigen_type()
        self.retrieve_parameters()

    def validate_arguments(self):
        if(self.df_eigenvals is None and self.df_pdf is None):
            raise ValueError(
                "RMTplot() expects at least one dataframe for the arguments."
            )

    def check_eigen_type(self):
        if self.df_eigenvals is not None:
            if np.count_nonzero(self.df_eigenvals['imag_part'].values) == 0:
                self.eigen_type = 'real'
            else:
                self.eigen_type = 'complex'
        elif self.df_pdf is not None:
            if np.count_nonzero(self.df_pdf['imag_part'].values) == 0:
                self.eigen_type = 'real'
            else:
                self.eigen_type = 'complex'

    def retrieve_parameters(self):
        non_params_cols = ['real_part', 'imag_part', 'density', 'group']
        p_keys = list(set(self.df_pdf.columns.values) - set(non_params_cols))
        p_ranges = [self.df_pdf[p_key].unique() for p_key in p_keys]
        self.params = OrderedDict(zip(p_keys, p_ranges))

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
            # plotlyServerURL="https://chart-studio.plotly.com",
            toImageButtonOptions=dict(
                format=self.save_img_as,
                filename='rmt',
                # height=600,
                # width=600,
                scale=1
            ),
            displayModeBar=True,
            displaylogo=False,
            staticPlot=False,
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
        else:
            config['scrollZoom'] = True

        return config

    def _create_layout(self):
        if self.theme == 'icon':
            layout = go.Layout(
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
                showlegend=False,
                margin=dict(
                    t=0,
                    b=0,
                    l=0,
                    r=0
                ),
                boxgap=1,
            )

        else:
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
                    b=45,  # Shift the same amount with l (min: 45)
                    l=55,  # Shift the same amount with b (min: 55)
                ),
                boxgap=1
            )

            if self.theme == 'matlab':
                layout.update(
                    dict(
                        xaxis=dict(
                            mirror='all',
                            showgrid=True, gridwidth=1, gridcolor='rgba(238, 238, 238, 1)',
                            zeroline=True, zerolinewidth=1, zerolinecolor='rgba(0, 0, 0, 1)',
                        ),
                        yaxis=dict(
                            mirror='all',
                            showgrid=True, gridwidth=1, gridcolor='rgba(238, 238, 238, 1)',
                            zeroline=True, zerolinewidth=1, zerolinecolor='rgba(0, 0, 0, 1)',
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

        # if self.slider:
        #     p_valpairs = [x for x in product(*self.params.values())]
        #     steps = []

        #     for i, p_valpair in enumerate(p_valpairs):
        #         print(i, p_valpair)
        #         step = dict(
        #             method="restyle",
        #             args=[{"visible": [False] * (len(p_valpairs))}],
        #             # args=[{"visible": False}],
        #         )
        #         # make only a current step visible
        #         step["args"][0]["visible"][i] = True
        #         steps.append(step)

        #     layout.update(
        #         sliders=[dict(
        #             active=0,
        #             pad={"t": 30},
        #             steps=steps
        #         )]
        #     )

        return layout
