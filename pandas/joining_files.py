import pandas as pd

df1= pd.read_csv('a.csv')
df2= pd.read_csv('b.csv')

# concat function to join dataframe
print(pd.concat([df1,df2], axis=0)) # stack rows

print(pd.concat([df1,df2], axis=1)) # stack columns

# merge
# types of merge- inner,outer,left,right

df_inner_join=pd.merge(df1,df2, on="student_id",how="inner")
df_inner_join.to_csv('df_inner_join_data.csv',index=False)

df_left_join=pd.merge(df1,df2, on="student_id",how="left")
df_left_join.to_csv('df_left_join_data.csv',index=False)