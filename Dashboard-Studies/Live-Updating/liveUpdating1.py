import dash
import dash_html_components as html
import requests

url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
# Update live session url in here {Live-Data URL of anything}

# A fake header is necessary to access the site
res = requests.get(url, headers={'Viewer': 'Mozilla/5.0'})
data = res.json()
counter = 0
for element in data["stats"]["total"]:
    counter += data["stats"]["total"][element]

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        html.Iframe(src = 'https://www.flightradar24.com', height = 500, width = 1200)
        # either a flight data or covid data anything can be provided
    ]),

    html.Div([
    html.Pre('Active Covid everyday: {}'.format(counter))
    ])
])

if __name__ == '__main__':
    app.run_server()