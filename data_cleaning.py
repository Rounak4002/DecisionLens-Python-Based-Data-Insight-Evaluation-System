import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)
    print("Data cleaning completed.")
    return df
