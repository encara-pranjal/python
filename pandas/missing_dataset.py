import pandas as pd

df= pd.read_csv(r'C:\Users\encar\Downloads\dataset.csv')
# print(df)

print(df.isna()) # false= record not missing
                 #true= record is missing
print(df.isna().sum())   

print(df.isna().sum()/ len(df)*100) # shows percentage of missing data

df['Product']= df['Product'].fillna('unknown')
print(df)

df['Price']=df['Price'].fillna(df['Price'].mean()) # in this we are filling mean of price column in the missing place
print(df)

df['Quantity']=df['Quantity'].fillna(df['Quantity'].median()) 
print(df)

df['Discount']=df['Discount'].fillna(0)
print(df)