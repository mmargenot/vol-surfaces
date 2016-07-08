import requests
import json
import re
import pandas as pd
import numpy as np
from scipy.stats import norm
#import matplotlib.mplot3d

URL1 = 'http://www.google.com/finance/option_chain?q=%s&output=json'
URL2 = 'http://www.google.com/finance/option_chain?q=%s&output=json&expy=%d&expm=%d&expd=%d' 

TRIALS = 1000
ERROR = 1/(1e9)

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
    
def calculate_all_vols(option_chain):
    """ Iterates and calculates the implied volatility
    for every option in the option chain
    
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
    local_option_chain = option_chain.copy()
    return
    
def calculate_implied_vol(option, underlying, strike, rf, tau, type):
    """ Uses the Black-Scholes Model and Brent's
    algorithm to calculate the implied volatility
    of an option.
    
    Parameters
    ----------
    option : float
        The market price of an option
    underlying : float
        The price of the underlying of that option
    strike : float
        The strike price of that option
    rf : float
        The risk free interest rate
    tau : float
        The time to maturity of an option
    type : char
        The type of the option (C or P (Call or Put))
    
    Returns
    -------
    implied_vol : float
        The calculated implied volatility of the
        option
    
    Initial guess for volatility calculation given by:
    http://www.eecs.harvard.edu/~parkes/cs286r/spring08/reading3/chambers.pdf
    
    Hopefully this converges
    sigma_{n+1} = sigma_n - (BS(sigma_n) - Option Price) / vega(sigma_n)
    """
    
    root_tau = np.sqrt(tau)
    root_2pi = 2.50662827463
    vol = (option/underlying) / (root_2pi/root_tau) # initial guess
    
    b = vol
    a = # Contrapoint to b?
    
    for trial in range(TRIALS):
        current_option = Option(underlying, strike, tau, rf, vol, type)
    
    
    sigma = 
    
    

    return
    
class Option:
    def __init__(self, S, K, tau, r, sigma, type):
        self.underlying = S
        self.strike = K
        self.ttm = tau
        self.risk_free
        self.vol = sigma
        self.type = type
        
    def calculate_price(self):
        """ Calculates the Black-Scholes price of the option """
        self.d1 = (1 / self.sigma / np.sqrt(self.ttm)) * (np.log(self.underlying / self.strike) +
            (self.risk_free + self.sigma * self.sigma / 2) * (self.ttm))
        self.d2 = self.d1 - self.sigma * self.sqrt(self.ttm)
        
        if self.type = 'C':
            price = self.underlying*norm.cdf(self.d1) - K*np.exp(-self.risk_free*self.ttm)*norm.cdf(self.d2)
        else:
            price = K*np.exp(-self.risk_free*self.ttm)*norm.cdf(-self.d2) - self.underlying*norm.cdf(-self.d1)
        return price
    
    def calculate_vega(self):
        """ Calculates the vega of the option """
        return self.underlying*np.sqrt(self.ttm)*norm.pdf(self.d1)
        
        
    