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
df.to_csv("processed_data.csv", index=False)