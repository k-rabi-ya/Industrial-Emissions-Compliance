import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("city_day.csv")
print(df.shape)
df.head()
df.tail()

df.info()
print(df.columns)
df.isnull().sum()
df.describe()
# Remove duplicate rows
duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

df = df.drop_duplicates()

# Check dataset structure
print(df.info())

# Remove unnecessary column
df = df.drop(['Date'], axis=1)

# Check missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing numeric values with mean
df = df.fillna(df.mean(numeric_only=True))

# Fill categorical column
df['AQI_Bucket'] = df['AQI_Bucket'].fillna('Unknown')

print("Missing values after cleaning:")
print(df.isnull().sum())

df.to_csv("processed_data.csv", index=False)