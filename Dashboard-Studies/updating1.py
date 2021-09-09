import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv(r'C:\Users\vkrishnamurthy\Desktop\Git\Python-Operations\Dashboard-Studies\Data\mpg.csv')
# Add a random "jitter" to model_year to spread out the plot
# A 'jitter' is a variant of strip plot with a better view of data points which is used to visualize many individual one dimensional values
df['year'] = random.randint(-4,5,len(df))*0.20 + df['model_year']

app.layout = html.Div([
    dcc.Graph(
        id='mpg_scatter',
        figure={
            'data': [go.Scatter(
                x = df['year']+1900,  # our "jittered" data
                y = df['mpg'],
                text = df['name'],
                hoverinfo = 'text',
                mode = 'markers'
            )],
            'layout': go.Layout(
                title = 'mpg.csv Data',
                xaxis = {'title': 'Model year'},
                yaxis = {'title': 'Miles per gallon'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()