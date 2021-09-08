import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

    # DROPDOWN https://dash.plot.ly/dash-core-components/dropdown
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Chennai', 'value': 'CH'},
            {'label': 'Mumbai', 'value': 'MI'},
            {'label': 'Banglore', 'value': 'BL'}
        ],
        value='MTL'
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Chennai', 'value': 'CH'},
            {'label': u'Mumbai', 'value': 'MI'},
            {'label': 'Banglore', 'value': 'BL'}
        ],
        value=['MI', 'CH'],
        multi=True
    ),

    # SLIDER https://dash.plot.ly/dash-core-components/slider
    html.Label('Slider'),
    html.P(
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        marks={i: i for i in range(-5,11)},
        value=1
    )),

    # RADIO ITEMS https://dash.plot.ly/dash-core-components/radioitems
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'Chennai', 'value': 'CH'},
            {'label': 'Mumbai', 'value': 'MI'},
            {'label': 'Banglore', 'value': 'BL'}
        ],
        value='CH'
    )
], style={'width': '50%'})

if __name__ == '__main__':
    app.run_server()