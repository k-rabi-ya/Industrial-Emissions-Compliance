import pandas as pd

def load_data():

    data2 = pd.read_excel("data/ghgp_data_2023.xlsx", skiprows=3)
    data3 = pd.read_excel("data/ghgp_data_2022.xlsx", skiprows=3)

    data = pd.concat([data2, data3], ignore_index=True)

    print("Data loaded successfully")

    return data