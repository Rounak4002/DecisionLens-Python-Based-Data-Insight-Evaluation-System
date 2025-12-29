def sql_analysis(df):
    print("\n--- SQL Style Analysis ---")

    print("\nHigh Sales Records (>13000):")
    print(df[df["sales"] > 13000])

    print("\nCategory-wise Sales:")
    print(df.groupby("category")["sales"].sum())
