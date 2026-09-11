import pandas as pd
df= pd.read_csv(r'C:\Users\encar\Downloads\career_choices_2026.csv')


print(df[df['Expected_Salary_LPA']>20])

print(df[df['Interested_in_Generative_AI']== "Yes"])

print(df[df['Preferred_Career_2026']== "Data Scientist"])

print(df['Expected_Salary_LPA'].mean())