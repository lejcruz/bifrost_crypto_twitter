from src import apiproperties, price, text, post_twitter

# RETRIEVE PRICE DATA FROM COINMARKETCAP API AND DISPLAY THE FIRST 10 CRYPTO SORTED BY MARKETCAP

# Global variables
TIMEZONE = 'America/Sao_Paulo'

# COINMARKETCAP API
COINAPI_KEY = apiproperties.COINMARKETCAP_API_KEY
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# TWITTER API
CONSUMER_KEY = apiproperties.CONSUMER_KEY
CONSUMER_SECRET = apiproperties.CONSUMER_SECRET

ACCESS_TOKEN = apiproperties.TWITTER_ACESS_TOKEN
ACCESS_SECRET = apiproperties.TWITTER_ACESS_SECRET

# price.py params
params = {
  'start': '1',
  'limit': '5000',
  'convert': 'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINAPI_KEY,
}

connection_params = {
  'url': URL,
  'headers': headers,
  'params': params
  }

format = {
  'currency': params['convert'],
  'sortby': 'MARKET_CAP'
  }


get_price_args = {
  'connect': connection_params,
  'format': format
  }

# text.py params

make_text_params = {
  'qty': 10,
  'text_prefix': "Last prices updates: \n\n"
}


def main():

    # get price
    prices = price.get_price(get_price_args)

    text_to_post = text.make_text(prices, **make_text_params)

    post_twitter.post_twitter(
      text_to_post,
      CONSUMER_KEY, CONSUMER_SECRET,
      ACCESS_TOKEN, ACCESS_SECRET)

    return text_to_post


if __name__ == "__main__":
    main()
