import yfinance as yf
from typing import List


def find_actives_informations(actives: List[str]):
    actives = list(map(lambda x: f'{x}.SA', actives))

    chamada = yf.download(tickers=actives, period='1y')

    if not chamada.empty:
        chamada = chamada['Adj Close'].reset_index()
        return chamada
    else:
        return None

    # fundo = yf.Tickers(tickers=actives)
    # print(fundo.history())


if __name__ == '__main__':
    from functions.dash_board_functions.dash_functions import create_dash

    data_informations = find_actives_informations(['BBSE3', 'VALE3', 'WEGE3', 'ITUB4', 'PETR4', 'ABEV3'])
    # print(data_informations)

    response = create_dash(data_informations)

    response.run_server(debug=True)
