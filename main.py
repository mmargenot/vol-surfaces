# Generate a vol-surface for a given option chain

import sys
import pandas as pd
import requests
import json
import re
from utils import json_decode
 
URL1 = 'http://www.google.com/finance/option_chain?q=%s&output=json'
URL2 = 'http://www.google.com/finance/option_chain?q=%s&output=json&expy=%d&expm=%d&expd=%d' 

def main(argv):
    """ Main function """
    # First get the name of the option we want
    symbol = argv[1]
    # Then pull the option chain from Google Finance    
    chain = get_option_chain(symbol)
    
    # Do some math
    # Generate a 3D plot on P x T x vol


def get_option_chain(symbol):
    """ Pulls the option chain from Google Finance.
    Should return as a Pandas Panel """
    url = URL1 % symbol
    response = requests.get(url)
    if response.status_code == 200:
        content_json = response.content
        content_json = content_json.decode('utf-8')
        data = re.sub('(\w+:)(\d+\.?\d)', r'\1"\2"', content_json)
        data = re.sub('(\w+):', r'"\1":', data)
        data = json.loads(data)
        return data
        
if __name__ == "__main__":
    main(sys.argv)