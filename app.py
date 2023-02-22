# Import libraries
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import dbx_utils

# Load the dataset
avocado = dbx_utils.get_line_data()

# Create the Dash app
dash_app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
app = dash_app.server

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=avocado['geography'].unique(),
                            value='New York')

dash_app.layout = html.Div(children=[
    html.H1(children='Avocado Prices Dashboard Updated'),
    geo_dropdown,
    dcc.Graph(id='price-graph')
])


# Set up the callback function
@dash_app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    return line_fig


# Run local server
if __name__ == '__main__':
    dash_app.run_server(debug=True)
