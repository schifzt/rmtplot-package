# -*- coding: utf-8 -*-
#!bin/python3

import plotly.graph_objects as go


def layout(icon):
    if icon:
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
                )
            )
        )
    else:
        return (
            go.Layout(
                dragmode='pan',
                hovermode='closest',
                xaxis=dict(
                    autorange=True, mirror='all', ticks='inside',
                    showgrid=False, showline=True, showticklabels=True,
                    linecolor='rgba(0, 0, 0, 1)', linewidth=2, tickwidth=2,
                    rangemode='tozero',
                    automargin=False
                ),
                yaxis=dict(
                    autorange=True, mirror='all', ticks='inside',
                    showgrid=False, showline=True, showticklabels=True,
                    linecolor='rgba(0, 0, 0, 1)', linewidth=2, tickwidth=2,
                    rangemode='tozero',
                    automargin=False
                ),
                paper_bgcolor='rgba(255, 255, 255, 0)',
                plot_bgcolor='rgba(255, 255, 255, 0)',
                legend=dict(
                              x=1, xanchor='right',
                              y=1
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
                )
            )
        )
