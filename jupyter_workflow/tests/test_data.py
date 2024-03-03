from jupyter_workflow.data import get_fremont_data
import pandas as pd
import numpy as np

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['Total', 'Northbound', 'Southbound'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)
    
