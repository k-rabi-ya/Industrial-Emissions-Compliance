import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def prepare_data():
    df = pd.read_csv("processed_ghg_data_singular.csv")

    # Engineering our target variable i.e compliance with respect to each industry
    industry_thresholds = df.groupby('Primary NAICS Code')['Total reported direct emissions'].transform(lambda x: x.quantile(0.85))
    
    # Flag non-compliant factories
    df['Compliance_Status'] = np.where(
        df['Total reported direct emissions'] > industry_thresholds, 1, 0
    )

    # AUDIT / DISCREPANCY DETECTION
    audit_threshold = df.groupby('Primary NAICS Code')['Total reported direct emissions'].transform(lambda x: x.quantile(0.95))

    df['Audit_Flag'] = np.where(
        df['Total reported direct emissions'] > audit_threshold, 1, 0
    )

    # Encode categorical data
    le = LabelEncoder()
    df['State'] = le.fit_transform(df['State'].astype(str))
    df['Primary NAICS Code'] = le.fit_transform(df['Primary NAICS Code'].astype(str))

    # Select features
    feature_cols = [
        'CO2 emissions (non-biogenic) ',
        'Methane (CH4) emissions ',
        'Nitrous Oxide (N2O) emissions ',
        'Primary NAICS Code',
        'State',
        'Reporting_Year',
        '2021 Total reported direct emissions',
        '2020 Total reported direct emissions'
    ]

    X = df[feature_cols]
    y = df['Compliance_Status']

    return X, y