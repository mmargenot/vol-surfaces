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
        
def generate_plot(vol_frame):
    
    return
    
def calculate_implied_vol(option_chain):
    option_chain = option_chain.copy()

    return