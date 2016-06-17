import requests
import json
import re
import pandas as pd

URL1 = 'http://www.google.com/finance/option_chain?q=%s&output=json'
URL2 = 'http://www.google.com/finance/option_chain?q=%s&output=json&expy=%d&expm=%d&expd=%d' 

def get_option_chain(symbol, option_type = None, expiry_month = None, expiry_year = None):
    """ Pulls the option chain from Google Finance.
    Should return as a Pandas Panel or DataFrame 
    
    Parameters
    ----------
    symbol : string
        Name of the underlying that we want the option
        chain for
        
    Returns
    -------
    data : pandas.DataFrame
        DataFrame with MultiIndex that contains all
        options for all expirations """
        
    url = URL1 % symbol
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Can't access Google!")
    
    content_json = response.content
    content_json = content_json.decode('utf-8')
    data = re.sub('(\w+:)(\d+\.?\d+)', r'\1"\2"', content_json)
    data = re.sub('(\w+):', r'"\1":', data)
    data = json.loads(data)

    # Parse data dict into a pd.DataFrame
    def parse_options_into_df(option_dict):
        """ Takes the option dictionary and turns it
        into a MultiIndex DataFrame """
        calls = option_dict['calls']
        calls = pd.DataFrame(calls)
        # Reindex the calls
        calls = calls.set_index(calls['expiry'])
        calls = calls.drop('expiry', 1)
        
        puts = option_dict['puts']
        puts = pd.DataFrame(puts)
        # Reindex the puts
        puts = puts.set_index(puts['expiry'])
        puts = puts.drop('expiry', 1)
        
        return pd.concat([calls, puts], keys = ['call', 'put'])
    
    option_df = parse_options_into_df(data)
    return option_df
    

        
def generate_plot(vol_frame):
    
    
    return
    
def calculate_implied_vol(option_chain):
    """ Uses the Black-Scholes Model (Bad model, I know)
    to calculate the implied volatility of all the
    options in a given option chain.
    
    Parameters
    ----------
    option_chain : pd.DataFrame
        DataFrame with MultiIndex that contains
        all options for all expirations 
    
    Returns
    -------
    vol_df : pd.DataFrame
        Probably a DataFrame with volatility, time to
        maturity, and strike price, organized by option
        type
    """
    option_chain = option_chain.copy()


    return