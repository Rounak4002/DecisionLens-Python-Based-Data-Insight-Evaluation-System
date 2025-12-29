from data_cleaning import clean_data
from eda import perform_eda
from sql_analysis import sql_analysis

df = clean_data("data/business_data.csv")
perform_eda(df)
sql_analysis(df)
