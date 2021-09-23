#!bin/python3

from context import sample
from context import rmtplot
import pandas as pd
import plotly.graph_objects as go
# from IPython.display import HTML
# from plotly.offline import init_notebook_mode, iplot
# init_notebook_mode()
# html_code = '''<script src="//cdnjs.cloudflare.com/ajax/libs/require.js/2.3.5/require.min.js"></script>'''
# HTML(html_code)

# sample.test()

df_pdf = pd.read_csv('Marchenko_Pastur/pdf.csv')
df_eigenvals = pd.read_csv('Marchenko_Pastur/eigenvals.csv')

blue = dict(
    line='rgba(0, 0, 255, 1)',
    fill='rgba(120, 120, 255, 0.75)'
)

red = dict(
    line='rgba(255, 0, 0, 1)',
    fill='rgba(255, 128, 128, 0.75)'
)

rmtplot = rmtplot.RMTplot(df_eigenvals, df_pdf, blue, 'matlab', False, False)
traces, layout, config = rmtplot.get_components()

fig = go.Figure()
fig.add_trace(traces.histogram1d)
fig.add_trace(traces.density1d)
fig.update_layout(layout)
fig.show(config=config, renderer='browser')
# iplot(fig)

# fig.export_to_html()
