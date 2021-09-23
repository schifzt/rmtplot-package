# -*- coding: utf-8 -*-
#!bin/python3

import plotly.graph_objects as go
from rmtplot.Traces import Traces
import importlib


class RMTplot:
    def __init__(
            self,
            df_eigenvals,
            df_pdf,
            color,
            *,
            theme='matlab',
            fill=False,
            icon=False,
            to_imege_format='svg'
    ):
        self.df_eigenvals = df_eigenvals
        self.df_pdf = df_pdf
        self.color = color
        self.theme = theme
        self.fill = fill
        self.icon = icon
        self.to_imege_format = to_imege_format

    def get_components(self):
        return self._create_traces(), self._create_layout(), self._create_config()

    def _create_traces(self):
        traces = Traces(
            self.df_eigenvals,
            self.df_pdf,
            self.color,
            self.fill
        )

        traces.fit()

        return traces

    def _create_layout(self):
        return importlib.import_module("rmtplot." + self.theme).layout(self.icon)

    def _create_config(self):
        config = dict(
            responsive=True,
            showSendToCloud=False,
            plotlyServerURL="https://chart-studio.plotly.com",
            toImageButtonOptions=dict(
                format=self.to_imege_format,
                filename='rmt',
                height=600,
                width=600,
                scale=1
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

        if self.icon:
            config['scrollZoom'] = False
            config['staticPlot'] = True
        else:
            config['scrollZoom'] = True
            config['staticPlot'] = False

        return config
