from multiprocessing import connection
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import pandas as pd
import pytz

# Connect to API and get json

def get_api_data_price(url, headers, params):

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=params)
        json_data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
    
    return json_data

# Data Formating
def format_data(json_data, currency, sortby='MARKET_CAP', time_zone='America/Sao_Paulo'):

    data_dict = json_data['data']

    # Put Data in pandas DataFrame
    appended_results = pd.DataFrame()

    for i in data_dict:

        __coin__ = i['name']
        __CoinSymbol__ = i['symbol']

        quote = i['quote'][currency]

        __price__ = quote['price']
        __volume__ = quote['volume_24h']
        __marketcap__ = quote['market_cap']
        __PercentChange1h__ = quote['percent_change_1h']

        __TimeUpdated__ = pd.to_datetime(quote['last_updated'])
        __TimeUpdated__ = __TimeUpdated__.astimezone(time_zone)
        

        __values__ = [__coin__, __CoinSymbol__, __price__, __marketcap__, __volume__, __PercentChange1h__, __TimeUpdated__]
        __cols__ = ['COIN_NAME', 'COINSYMBOL', 'PRICE', 'MARKET_CAP', 'VOLUME_LAST_24H', 'PERCENT_CHANGE_1H', 'TIME_UPDATED']

        __results__ = pd.DataFrame( [__values__],  
                                    columns = __cols__)

        appended_results = pd.concat([appended_results, __results__])

    appended_results.sort_values(sortby, ascending=False, inplace=True)

    return appended_results


def get_price(args):

    connection_params = args['connect']
    format_params = args['format']

    json_data = get_api_data_price(**connection_params)

    prices = format_data(json_data =json_data,  **format_params)

    return prices

