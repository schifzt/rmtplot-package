#!bin/python3
# https: // stackoverflow.com/questions/55220935/plotly-how-to-plot-a-cumulative-steps-histogram

import plotly.graph_objects as go
import numpy as np
import pandas as pd
from context import rmtplot


np.random.seed(1)

x = np.random.randn(500)

trace1 = go.Histogram(
    x=x,
    histnorm='probability density',
    marker=dict(
        line=dict(
            width=1,
        ),
        pattern=dict(
            # fillmode='overlay',
            fillmode='replace',
        )
    ),
    xbins=dict(
        size=0.1
    ),
)

layout = go.Layout(
    dragmode='pan',
    xaxis=dict(
        showgrid=False,
        zeroline=True, zerolinewidth=5, zerolinecolor='rgba(0, 0, 0, 1)',
        showline=True, linewidth=2, linecolor='rgba(0, 0, 0, 1)',
        showticklabels=True, ticks='inside',
        autorange=True, rangemode='normal',
        automargin=False,
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=True, zerolinewidth=5, zerolinecolor='rgba(0, 0, 0, 1)',
        showline=True, linewidth=2, linecolor='rgba(0, 0, 0, 1)',
        showticklabels=True, ticks='inside',
        autorange=True, rangemode='tozero',
        automargin=False,
    ),
    xaxis_title=r'$\lambda$',
    yaxis_title=r'$p(\lambda)$'
)

config = dict(
    showSendToCloud=False,
    displayModeBar=True,
    displaylogo=False,
    responsive=True,
)


fig = go.Figure()
fig.add_trace(trace1)
fig.update_layout(layout)
fig.show(config=config, renderer='browser')
