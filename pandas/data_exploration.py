import pandas as pd

df= pd.read_csv(r'C:\Users\encar\Downloads\career_choices_2026.csv')

print(df)
print(df.head()) #shows frist 5 records
print(df.tail()) #shows last 5 records

print(df.head(2))

print(df.shape)

print(df.columns)

print(df.info())