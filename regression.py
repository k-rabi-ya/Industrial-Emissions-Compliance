import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np

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

# Features and target
X = data.drop('Total reported direct emissions', axis=1)
y = data['Total reported direct emissions']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardization
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Linear Regression Model
model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Metrics
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)

print("R2 Score:", r2)
print("MSE:", mse)
print("RMSE:", rmse)
print("MAE:", mae)