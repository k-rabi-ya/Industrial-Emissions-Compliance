import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data2 = pd.read_excel("data/ghgp_data_2023.xlsx", skiprows=3)
data3 = pd.read_excel("data/ghgp_data_2022.xlsx", skiprows=3)

data = pd.concat([data2, data3], ignore_index=True)

data = data[[
'Total reported direct emissions',
'CO2 emissions (non-biogenic) ',
'Methane (CH4) emissions ',
'Nitrous Oxide (N2O) emissions '
]]

data = data.dropna()

# Histogram
plt.figure()
sns.histplot(data['Total reported direct emissions'], bins=30)
plt.title("Distribution of Total Emissions")
plt.show()

# Correlation heatmap
plt.figure()
sns.heatmap(data.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Scatter plot
plt.figure()
sns.scatterplot(
    x='CO2 emissions (non-biogenic) ',
    y='Total reported direct emissions',
    data=data
)
plt.title("CO2 vs Total Emissions")
plt.show()