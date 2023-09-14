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
            html.A("Rating Correlation", href="/options/option1", style=custom_styles['nav_link']),
            html.A("Rating History", href="/options/option2", style=custom_styles['nav_link']),
            html.A(" Castling & Rooks", href="/options/option3", style=custom_styles['nav_link']),
            html.A("Bishops vs Knights", href="/options/option4", style=custom_styles['nav_link']),
            html.A("Openings", href="/options/option5", style=custom_styles['nav_link']),
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
        html.H1("Rating Correlation", style={'margin-right': '20px'}),
        html.P("This is the content for Rating Correlation.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 2 content
option2_layout = html.Div([
    html.Div([
        html.H1("Rating History", style={'margin-right': '20px'}),
        html.P("This is the content for Rating History.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 3 content
option3_layout = html.Div([
    html.Div([
        html.H1("Castling & Rooks", style={'margin-right': '20px'}),
        html.P("This is the content for Castling & Rooks.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}),

# Layout for Option 4 content
option4_layout = html.Div([
    html.Div([
        html.H1(" Bishops vs. Knights", style={'margin-right': '20px'}),
        html.P("This is the content for Bishops vs. Knights.", style={'font-size': '24px'}),
    ], style={'display': 'flex', 'align-items': 'center'}),
], style={'background-image': 'linear-gradient(to Bottom, gray, white)', 'color': 'black', 'padding': '10px',
          'display': 'flex', 'justify-content': 'link', 'align-items': 'center'}, )

# Layout for Option 5 content
option5_layout = html.Div([
    html.Div([
        html.H1("Openings", style={'margin-right': '20px'}),
        html.P("This is the content for Openings.", style={'font-size': '24px'}),
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

    elif pathname == '/':
        return home_layout
    else:
        raise PreventUpdate


# Callback to update the graph content based on URL pathname
@app.callback(

    Output('graph-content', 'children'),
    Input('url', 'pathname')
)
def update_graph(pathname):
    if pathname == '/':
        return html.Div([
            html.H3("About us ", style={'font-size': '24px'}),
            html.P("Lichess.org is a free online chess website, that facilitates matches"
                   "against random players all over the world."
                   "Games are available in different Game-Modes, including Bullet, Blitz,"
                   "Classical and Rapid."
                   "The main difference between them is their duration."
                   "For our analysis we have mainly focused on the game-mode Rapid,"
                   "where players only have 10 minutes each to make all of their moves in the entire game."
                   "A player loses if their king is checkmated or if they run out of time."
                   "Our project is aimed at answering some questions regarding players’ improvement and game strategies. For this purpose we analyzed"
                   "approximately 32,000 high-rated rapid games, roughly 122,000 amateur rapid matches and almost 700,000 high-rated blitz games. ")])

    elif pathname == '/options/option1':
        with open("number_of_games.json", "r") as file:
            number_of_games_fig = pio.from_json(file.read())
        with open("number_of_puzzles.json", "r") as file:
            number_of_puzzles = pio.from_json(file.read())
        with open("puzzle_rating.json", "r") as file:
            puzzle_rating = pio.from_json(file.read())

        return html.Div([
            dcc.Graph(id='option1-chart-1', figure=number_of_games_fig),
            dcc.Graph(id='option1-chart-2', figure=number_of_puzzles),
            dcc.Graph(id='option1-chart-3', figure=puzzle_rating)])

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
        with open("1_a_castling_early_VIOLIN.json", "r") as file:
            fig1_a = pio.from_json(file.read())
        with open("2_a_rook_act_early_VIOLIN.json", "r") as file:
            fig2_a = pio.from_json(file.read())
        with open("3_a_castle_which_side_BAR.json", "r") as file:
            fig3_a = pio.from_json(file.read())

        return html.Div([
            html.H3("Does castling early help to win a match?"),
            dcc.Graph(id='option3-chart-1', figure=fig1_a),
            html.H3("Do the games in which the rooks are activated early result in a win?"),
            dcc.Graph(id='option3-chart-2', figure=fig2_a),
            html.H3("Castling on which side results in a win? How does castling affect the outcome of a game?"),
            dcc.Graph(id='option3-chart-3', figure=fig3_a)])

    elif pathname == '/options/option4':
        with open("4_a_bishop_vs_knight_BAR.json", "r") as file:
            fig4_a = pio.from_json(file.read())

        return html.Div([
            html.H3("Does having bishops or knights during an endgame result in a win?"),
            dcc.Graph(id='option4-chart-1', figure=fig4_a),
        ])

    elif pathname == '/options/option5':
        with open("5_a_opening_game_mode_MULT_PIE.json", "r") as file:
            fig5_a = pio.from_json(file.read())
        with open("6_a_opening_elo_HEATMAP.json", "r") as file:
            fig6_a = pio.from_json(file.read())
        with open("6_b_opening_elo_SCATTER_CAT.json", "r") as file:
            fig6_b = pio.from_json(file.read())

        return html.Div([

            html.H3("What openings are played by the groups of players belonging to different game modes?"),
            dcc.Graph(id='option5-chart-1', figure=fig5_a),
            html.H3("What openings are played by the groups of players belonging to different rating categories?"),
            dcc.Graph(id='option5-chart-2', figure=fig6_a),
            dcc.Graph(id='option5-chart-3', figure=fig6_b),
            html.P("Visit this link for information about openings categorization."),
            html.A('https://www.chessprogramming.org/ECO', href='https://www.chessprogramming.org/ECO',
                   style=custom_styles['nav_link']),

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
