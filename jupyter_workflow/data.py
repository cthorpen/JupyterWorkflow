import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/resource/65db-xm6k.csv$limit=50000'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """
    download and cache the fremont data
    
    params:
    -----
    filename: string (optional)
    url: strong (optional)
    force_download: bool (optional)
        if true, force redownload of data
        
    returns:
    -----
    data: pandas.DataFrame
        the fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='date', parse_dates=True)
    data.columns = ['Total', 'Northbound', 'Southbound']
    return data