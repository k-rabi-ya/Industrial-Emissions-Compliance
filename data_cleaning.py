import pandas as pd

def clean_data(data):

    data = data[[
        'Total reported direct emissions',
        'CO2 emissions (non-biogenic) ',
        'Methane (CH4) emissions ',
        'Nitrous Oxide (N2O) emissions '
    ]]

    for col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    data = data.fillna(data.median())

    print("Data cleaning completed")

    return data