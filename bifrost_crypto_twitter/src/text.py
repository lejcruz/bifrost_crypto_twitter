import pandas as pd

# Make Text
def make_text(df, qty, text_prefix='Last prices updates: \n\n'):

    df = df.head(qty)

    text = ''
    for row in df.iterrows():

        __row__ = row[1]

        __symbol__ = __row__['COINSYMBOL']
        __price__ = '{:,.3f}'.format(__row__['PRICE'])
        __PercentChangeNum__ = __row__['PERCENT_CHANGE_1H']
        __PercentChangeChar__ = '{:.2f}%'.format(__PercentChangeNum__)

        if __PercentChangeNum__ < 0:
            __heart__ = "\ud83d\udc94"  

        elif __PercentChangeNum__ > 0:
            __heart__ = "\ud83d\udc9a"      
        
        elif __PercentChangeNum__ == 0:
            __heart__ = "\ud83e\udd0d"   
        
        __text__ = "#" + __symbol__ + ": $" + __price__ + " " + __PercentChangeChar__ + " " + __heart__ + '\n'

        text = text + __text__

    text = text_prefix + text
    
    return text