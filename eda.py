def perform_eda(df):
    print("\n--- Exploratory Data Analysis ---")
    print("\nPreview:")
    print(df.head())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\nSales by Region:")
    print(df.groupby("region")["sales"].sum())
