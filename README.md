Bifrost Crypto Twitter
================
!['alttext'](https://img.shields.io/github/languages/top/lejcruz/bifrost_crypto_twitter)

This project gets prices data from the CoinMarketCap API, then select the top 10 coins ordered by market cap and structure it in a text putting markers (hearts) according to the price behaviour. Then it posts the text to the https://twitter.com/Bifrost_Crypto account.

This code is meant to be deployed at AWS and run every 60 minutes (in construction)

Usage
------------

This project was built with Python 3.9.10, make sure to have this version in your venv and install the packages from the requirements.txt

To work it's needed to register at https://coinmarketcap.com/api/ and https://developer.twitter.com/ and put the API keys to the bifrost_crypto_twitter/src/apiproperties.py. IT'S VERY IMPORTANT TO NEVER PUSH THIS FILE TO GITHUB.


    # twitter keys

    BEARER_TOKEN = ''

    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''

    TWITTER_ACESS_TOKEN = ''
    TWITTER_ACESS_SECRET = ''

    # coinmarketcap keys
    COINMARKETCAP_API_KEY = ''

Params
------------

It's possible to change some parameters like currency and quantity of coins displayed.
To change the currency, modify the 'convert' in the 'params' dictionary in the app.py to currency suported by the coinmarketcap API

    params = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
    }

To change the max quantity displayed, modify the 'qty' in the 'make_text_params' dictionary in the app.py. It's important to respect the maximum character limitation of twitter.

    make_text_params = {
    'qty': 10,
    'text_prefix': "Last prices updates: \n\n"
    }