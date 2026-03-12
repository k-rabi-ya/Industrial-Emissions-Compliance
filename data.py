import pandas as pd


df_2023 = pd.read_excel("ghgp_data_2023.xlsx", sheet_name="Direct Point Emitters", skiprows=3)
df_2023['Reporting_Year'] = 2023  # Tag these rows as 2023 data

df_2022 = pd.read_excel("ghgp_data_2022.xlsx", sheet_name="Direct Point Emitters", skiprows=3)
df_2022['Reporting_Year'] = 2022  # Tag these rows as 2022 data

# Stack them vertically to double the training data
combined_df = pd.concat([df_2023, df_2022], ignore_index=True)

# Load the historical "By Year" dataset to get older baselines
df_history = pd.read_excel("ghgp_data_by_year_2023.xlsx", sheet_name="Direct Point Emitters", skiprows=3)
# Keep only the Facility ID and older years for historical context
history_cols = ['Facility Id', '2021 Total reported direct emissions', '2020 Total reported direct emissions']
df_history_subset = df_history[history_cols]

# Merge the historical data into our combined dataset using 'Facility Id'
final_df = pd.merge(combined_df, df_history_subset, on='Facility Id', how='left')

# --- CLEANING ---
# Drop columns that aren't useful
columns_to_drop = ['FRS Id', 'Facility Name', 'Address', 'Zip Code', 'City', 'County', 'Latitude', 'Longitude']
final_df = final_df.drop(columns=columns_to_drop, errors='ignore')

# Convert emission columns to numeric, filling blanks with 0
emission_cols = [
    'Total reported direct emissions', 
    'CO2 emissions (non-biogenic) ', 
    'Methane (CH4) emissions ', 
    'Nitrous Oxide (N2O) emissions ',
    '2021 Total reported direct emissions',
    '2020 Total reported direct emissions'
]

for col in emission_cols:
    final_df[col] = pd.to_numeric(final_df[col], errors='coerce').fillna(0)

final_df.to_csv("processed_ghg_data_singular.csv", index=False)
print(f"Success! Singular dataset created with shape: {final_df.shape}")