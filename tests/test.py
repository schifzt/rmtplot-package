#!bin/python3

from context import rmtplot
from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objects as go

# from IPython.display import HTML
# from plotly.offline import init_notebook_mode, iplot
# init_notebook_mode()
# html_code = '''<script src="//cdnjs.cloudflare.com/ajax/libs/require.js/2.3.5/require.min.js"></script>'''
# HTML(html_code)


blue = dict(
    line='rgba(0, 0, 255, 1)',
    fill='rgba(120, 120, 255, 0.8)',
    border='rgba(120, 120, 255, 0.8)',
    rug='rgba(255, 255, 255, 1)',
)

red = dict(
    line='rgba(255, 0, 0, 1)',
    fill='rgba(255, 128, 128, 0.8)',
    border='rgba(255, 128, 128, 0.8)',
    rug='rgba(255, 255, 255, 1)'
)

lavender = dict(
    line='rgba(255, 0, 0, 1)',
    fill='rgba(222, 229, 240, 0.8)',
    border='rgba(133, 160, 199, 1)',
    rug='rgba(133, 160, 199, 1)'
)


target = 'Marchenko_Pastur'
# target = 'Semicircle_Law'
target = 'Circular_Law'
# target = 'Kronecker'


df_pdf = pd.read_csv(target + '/pdf.csv')
df_eigenvals = pd.read_csv(target + '/eigenvals.csv')


rmtplot = rmtplot.RMTplot(df_eigenvals, df_pdf,
                          color=lavender,
                          theme='matlab',
                          fill=False,
                          gridline=True)

traces, layout, config = rmtplot.get_components()


fig = go.Figure(data=traces.data, layout=layout)

fig.update_layout(layout)

# fig.show(config=config, renderer='browser')
# iplot(fig)
fig.write_html(target + '.html',
               config=config,
               include_plotlyjs='cdn',
               include_mathjax='cdn',
               full_html=True,
               auto_open=True,
               )
