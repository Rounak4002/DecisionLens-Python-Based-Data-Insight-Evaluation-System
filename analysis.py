import pandas as pd

# Load dataset
df = pd.read_csv("data/business_data.csv")

# Data cleaning
df.drop_duplicates(inplace=True)

# Display dataset preview
print("Dataset Preview:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Exploratory Data Analysis
print("\nTotal Sales by Region:")
print(df.groupby("region")["sales"].sum())
