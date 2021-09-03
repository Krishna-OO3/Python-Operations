# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# colors = {
#     'background': '#1111111',
#     'text': '#7FDBFF'
# }

# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

# app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#     html.H1(
#         children='Hello Dash',
#         style={
#             'textAlign': 'center',
#             'color': colors['text']
#         }
#     ),

#     html.Div(children='Dash: A web application framework for Python.', style={
#         'textAlign': 'center',
#         'color': colors['text']
#     }),

#     dcc.Graph(
#         id='example-graph-2',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# fig = px.scatter(df, x="gdp per capita", y="life expectancy",
#                  size="population", color="continent", hover_name="country",
#                  log_x=True, size_max=60)

# app.layout = html.Div([
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

# import dash
# import time
# from datetime import datetime
# from dash.dependencies import Input, Output
# import dash_html_components as html
# from dash_html_components.Button import Button

# app = dash.Dash()
# app.layout = html.Div(
#     [
#         html.Button("execute callback", id="button_1"),
#         html.Button("execute slow callback", id="button_2"),
#         html.Div(children="callback not executed", id="first-output"),
#         html.Div(children="callback not executed", id="second-output"),
#     ]
# )

# @app.callback(
#     Output("first-output", "children"),
#     Input("button_1", "n_clicks"))
# def first_callback(n):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     return "in the fast callback it is : " + current_time 

# @app.callback(
#     Output("Second-output","children"),
#     Input("button_2", "n_clicks")
# )
# def second_callback(n):
#     time.sleep(5)
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     return "in the slow callback it is : " + current_time 

# if __name__ == '__main__':
#     app.run_server(debug=True)


# import dash
# from dash.dependencies import Input, Output
# import dash_html_components as html
# from datetime import datetime
# import time

# app = dash.Dash()
# app.layout = html.Div(
#     [
#         html.Button("execute fast callback", id="button_3"),
#         html.Button("execute slow callback", id="button_4"),
#         html.Div(children="callback not executed", id="first_output_3"),
#         html.Div(children="callback not executed", id="second_output_3"),
#         html.Div(children="callback not executed", id="third_output_3"),
#     ]
# )

# @app.callback(
#     Output("first_output_3", "children"),
#     Input("button_3", "n_clicks"))
# def first_callback(n):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     return "in the fast callback it is " + current_time

# @app.callback(
#     Output("second_output_3", "children"), Input("button_4", "n_clicks"))
# def second_callback(n):
#     time.sleep(5)
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     return "in the slow callback it is " + current_time

# @app.callback(
#     Output("third_output_3", "children"),
#     Input("first_output_3", "children"),
#     Input("second_output_3", "children"))
# def third_callback(n, m):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     return "in the third callback it is " + current_time

# if __name__ == '__main__':
#     app.run_server(debug=True)


import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Slider(
            id="slider-circular", min=0, max=20, 
            marks={i: str(i) for i in range(21)}, 
            value=3
        ),
        dcc.Input(
            id="input-circular", type="number", min=0, max=20, value=3
        ),
    ]
)

@app.callback(
    Output("input-circular", "value"),
    Output("slider-circular", "value"),
    Input("input-circular", "value"),
    Input("slider-circular", "value"),
)
def callback(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-circular" else slider_value
    return value, value

if __name__ == '__main__':
    app.run_server(debug=True)