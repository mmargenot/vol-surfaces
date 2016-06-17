# Generate a vol-surface for a given option chain

import sys
import pandas as pd
from utils import get_option_chain

def main(argv):
    """ Main function """
    # First get the name of the option we want
    symbol = argv[1]
    # Then pull the option chain from Google Finance    
    chain = get_option_chain(symbol)
    
    # Do some math
    # Generate a 3D plot on P x T x vol

    
if __name__ == "__main__":
    main(sys.argv)