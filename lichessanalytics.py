import webbrowser
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
import plotly.io as pio
from dash.exceptions import PreventUpdate

# Initialize the Dash app
app = Dash(__name__)
server = app.server
# Define custom CSS styles
custom_styles = {
    'navbar': {
        'background-image': 'linear-gradient(to left, black, white)',
        'color': 'white',
        'padding': '10px',
        'display': 'flex',
        'justify-content': 'link',
        'align-items': 'center',
        'position': 'relative',
    },
    'nav_links': {
        'list-style': 'none',
        'margin': '0',
        'padding': '0',
    },
    'nav_link': {
        'text-decoration': 'none',
        'color': 'inherit',
        'margin-right': '60px',
        'font-weight': 'bold',
    },

}

# Layout of the home page
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.Div([
        html.Img(src="/assets/lichesslogo.png", alt="foto", width="15%", lang="15%",
                 style={'position': 'absolute', 'top': '0px', 'right': '0px'}),
    ]),
    html.Nav(
        children=[
            html.A("Home", href="/", style=custom_styles['nav_link']),
            html.A("Option 1", href="/options/option1", style=custom_styles['nav_link']),
            html.A("Option 2", href="/options/option2", style=custom_styles['nav_link']),
            html.A("Option 3", href="/options/option3", style=custom_styles['nav_link']),
            html.A("Option 4", href="/options/option4", style=custom_styles['nav_link']),
            html.A("Option 5", href="/options/option5", style=custom_styles['nav_link']),
            html.A("Option 6", href="/options/option6", style=custom_styles['nav_link']),
            html.A("Option 7", href="/options/option7", style=custom_styles['nav_link']),
            html.A("Option 8", href="/options/option8", style=custom_styles['nav_link']),
        ],
        style={'background-image': 'linear-gradient(to left, black, white)', 'color': 'black', 'padding': '10px',
               'display': 'flex', 'justify-content': 'link', 'align-items': 'center'},
    ),
    html.Div(id='graph-content', style={'text-align': 'center', 'margin-top': '150px'}),

])

# Layout of the home page content
home_layout = html.Div([
    html.Div([
        html.H1("Welcome to Data Science Project Lichess Page", style={'margin-right': '20px'}),
    ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'}),
    html.P("Team: Michel, Mohamad, Viktoria.", style={'font-size': '24px'}),
], style={'background-image': 'linear-gradient(to bottom, gray, white)', 'color': 'black', 'padding': '10px'})

# Layout for Option 1 content
option1_layout = html.Div([
    html.Div([
        html.H1("Option 1", style={'margin-right': '20px'}),
        html.P("This is the content for Option 1.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 2 content
option2_layout = html.Div([
    html.Div([
        html.H1("Option 2", style={'margin-right': '20px'}),
        html.P("This is the content for Option 2.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 3 content
option3_layout = html.Div([
    html.Div([
        html.H1("Option 3", style={'margin-right': '20px'}),
        html.P("This is the content for Option 3.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )
# Layout for Option 4 content
option4_layout = html.Div([
    html.Div([
        html.H1("Option 4", style={'margin-right': '20px'}),
        html.P("This is the content for Option 4.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 5 content
option5_layout = html.Div([
    html.Div([
        html.H1("Option 5", style={'margin-right': '20px'}),
        html.P("This is the content for Option 5.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 6 content
option6_layout = html.Div([
    html.Div([
        html.H1("Option 6", style={'margin-right': '20px'}),
        html.P("This is the content for Option 6.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 7 content
option7_layout = html.Div([
    html.Div([
        html.H1("Option 7", style={'margin-right': '20px'}),
        html.P("This is the content for Option 7.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 8 content
option8_layout = html.Div([
    html.Div([
        html.H1("Option 8", style={'margin-right': '20px'}),
        html.P("This is the content for Option 8.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )


# Callback function to display the appropriate content based on URL pathname
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/options/option1":
        return option1_layout
    elif pathname == "/options/option2":
        return option2_layout
    elif pathname == "/options/option3":
        return option3_layout
    elif pathname == "/options/option4":
        return option4_layout
    elif pathname == "/options/option5":
        return option5_layout
    elif pathname == "/options/option6":
        return option6_layout
    elif pathname == "/options/option7":
        return option7_layout
    elif pathname == "/options/option8":
        return option8_layout

    else:
        return home_layout


# Callback to update the graph content based on URL pathname
@app.callback(
    Output('graph-content', 'children'),
    Input('url', 'pathname')
)
def update_graph(pathname):
    if pathname == '/options/option1':
        with open("/home/mohamad/Documents/UNI Kiel/DSProj/lichess_analytics/number_of_games_fig.json", "r") as file:
            number_of_games_fig = pio.from_json(file.read())

        return html.Div([
            dcc.Graph(id='option1-chart', figure=number_of_games_fig),
            dcc.Graph(id='option1-chart',
                      figure={
                          'data': [
                              go.Scatter(
                                  x=[1, 2, 3, 4, 5],
                                  y=[10, 11, 12, 13, 14],
                                  mode='markers',
                                  name='Option 1 Data',
                              ),
                          ],
                          'layout': {
                              'title': 'Option 1 Chart',
                          },
                      }),
            dcc.Graph(
                id='option1-chart',
                figure={
                    'data': [
                        go.Scatter(
                            x=[1, 2, 3, 4, 5],
                            y=[10, 11, 12, 13, 14],
                            mode='markers',
                            name='Option 1 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 1 Chart',
                    },
                }

            )
        ])
    elif pathname == '/options/option2':

        return html.Div([
            dcc.Graph(id='option2-chart',
                      figure={
                          'data': [
                              go.Scatter(
                                  x=[1, 2, 3, 4, 5],
                                  y=[10, 11, 12, 13, 14],
                                  mode='markers',
                                  name='Option 2 Data',
                              ),
                          ],
                          'layout': {
                              'title': 'Option 2 Chart',
                          },
                      }),
            dcc.Graph(id='option2-chart',
                      figure={
                          'data': [
                              go.Scatter(
                                  x=[1, 2, 3, 4, 5],
                                  y=[10, 11, 12, 13, 14],
                                  mode='markers',
                                  name='Option 2 Data',
                              ),
                          ],
                          'layout': {
                              'title': 'Option 2 Chart',
                          },
                      }),
            dcc.Graph(
                id='option2-chart',
                figure={
                    'data': [
                        go.Scatter(
                            x=[1, 2, 3, 4, 5],
                            y=[10, 11, 12, 13, 14],
                            mode='markers',
                            name='Option 2 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 2 Chart',
                    },
                }

            )
        ])
    elif pathname == '/options/option3':
        return html.Div([
            dcc.Graph(
                id='option3-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 3 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 3 Chart',
                    },
                }),
            dcc.Graph(
                id='option3-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 3 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 3 Chart',
                    },
                }),
            dcc.Graph(
                id='option3-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 3 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 3 Chart',
                    },
                }

            )
        ])

    elif pathname == '/options/option4':
        return html.Div([
            dcc.Graph(
                id='option4-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 4 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 4 Chart',
                    },
                }),
            dcc.Graph(
                id='option4-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 4 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 3 Chart',
                    },
                }),
            dcc.Graph(
                id='option4-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 4 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 4 Chart',
                    },
                }

            )
        ])
    elif pathname == '/options/option5':
        return html.Div([
            dcc.Graph(

                id='option5-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 5 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 5 Chart',
                    },
                }),
            dcc.Graph(

                id='option5-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 5 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 5 Chart',
                    },
                }),
            dcc.Graph(

                id='option5-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 5 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 5 Chart',
                    },
                }
            )
        ])
    elif pathname == '/options/option6':
        return html.Div([
            dcc.Graph(
                id='option6-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 6 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 6 Chart',
                    },
                }),
            dcc.Graph(
                id='option6-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 6 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 6 Chart',
                    },
                }),
            dcc.Graph(
                id='option6-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 6 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 6 Chart',
                    },
                }
            )
        ])
    elif pathname == '/options/option7':
        return html.Div([
            dcc.Graph(
                id='option7-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 7 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 7 Chart',
                    },
                }),
            dcc.Graph(
                id='option7-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 7 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 7 Chart',
                    },
                }),
            dcc.Graph(
                id='option7-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 7 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 7 Chart',
                    },
                }
            )
        ])
    elif pathname == '/options/option8':
        return html.Div([
            dcc.Graph(
                id='option8-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 8 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 8 Chart',
                    },
                }),
            dcc.Graph(
                id='option8-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 8 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 8 Chart',
                    },
                }),
            dcc.Graph(
                id='option8-chart',
                figure={
                    'data': [
                        go.Pie(
                            labels=['Category A', 'Category B', 'Category C'],
                            values=[40, 30, 20],
                            name='Option 8 Data',
                        ),
                    ],
                    'layout': {
                        'title': 'Option 8 Chart',
                    },
                }
            )
        ])
    else:
        raise PreventUpdate


if __name__ == '__main__':
    webbrowser.open_new_tab('http://localhost:8050')
    app.run_server(debug=True)
