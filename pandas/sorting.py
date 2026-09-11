import pandas as pd

df = pd.read_csv(r'C:\Users\encar\Downloads\career_choices_2026.csv')

print(df.sort_values("Expected_Salary_LPA",ascending=False)) #descending order

print(df.sort_values("Expected_Salary_LPA",ascending=True))# ascending order

print(df.sort_values("Expected_Salary_LPA")) #default value i.e. ascending=true
      
print(df.sort_values("Expected_Salary_LPA",ascending=False).head())