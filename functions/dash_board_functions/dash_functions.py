from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd


def create_dash(data):
    dash_app = Dash(__name__)

    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    @dash_app.callback(
        Output('grafico_ativos', 'figure'),
        Input('lista_tickers', 'value')
    )
    def update_graph(selected_tickers):
        # Se não houver tickers selecionados, mostra todos
        if not selected_tickers or 'Todos' in selected_tickers:
            df_plot = df
        else:
            df_plot = df[selected_tickers]

        # Criar gráfico de linhas
        fig_function = px.line(df_plot, x=df_plot.index, y=df_plot.columns,
                               labels={'value': 'Preço', 'variable': 'Ticker'},
                               title='Preços dos Tickers ao Longo do Tempo')

        # OBS¹: Quando usamos y=df_plot.columns, cada linha no gráfico representa uma coluna diferente do DataFrame.
        # OBS²: labels={'value': 'Preço', 'variable': 'Ticker'}: Permite personalizar os rótulos dos eixos e das
        # legendas no gráfico, tornando a visualização mais intuitiva e fácil de entender.

        return fig_function

    # Configurar opções do dropdown
    tickers = df.columns.tolist()
    tickers.append('Todos')

    dash_app.layout = html.Div(children=[
        html.H1(children='Dashboard de Tickers'),

        html.Div(children='Selecione os tickers para visualizar:'),

        dcc.Dropdown(tickers, value='Todos', id='lista_tickers', multi=True),

        dcc.Graph(id='grafico_ativos')
    ])

    return dash_app
