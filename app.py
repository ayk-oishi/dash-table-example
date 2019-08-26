import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd







########### Define your variables ######
myheading = "Wine Informationnnnn"
mysubheading = "August 2019"
tabtitle = 'Winelover'
filename = 'wine.csv'
sourceurl = 'https://raw.githubusercontent.com/ayk-oishi/dash-table-example/master/wine.csv'
githublink = 'https://github.com/ayk-oishi/dash-table-example'

########### Set up the data
df = pd.read_csv(filename)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H3(mysubheading),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),

    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    html.Br(),
    html.A("Plotly Dash", href='https://plot.ly/python/pie-charts/')
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
