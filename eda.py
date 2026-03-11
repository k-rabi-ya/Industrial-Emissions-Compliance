import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed dataset
df = pd.read_csv("processed_data.csv")

# Basic dataset inspection
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# AQI distribution
plt.figure(figsize=(6,4))
sns.histplot(df['AQI'], kde=True)
plt.title("AQI Distribution")
plt.xlabel("AQI")
plt.ylabel("Count")
plt.show()

# PM2.5 distribution
plt.figure(figsize=(6,4))
sns.boxplot(x=df['PM2.5'])
plt.title("PM2.5 Distribution")
plt.show()

# PM10 distribution
plt.figure(figsize=(6,4))
sns.histplot(df['PM10'], kde=True)
plt.title("PM10 Distribution")
plt.show()

# AQI category count
plt.figure(figsize=(8,5))
sns.countplot(x='AQI_Bucket', data=df)
plt.title("AQI Bucket Distribution")
plt.xticks(rotation=45)
plt.show()

# Correlation heatmap
plt.figure(figsize=(12,8))
correlation = df.corr(numeric_only=True)

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()