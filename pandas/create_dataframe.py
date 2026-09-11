import pandas as pd 
df1= pd.DataFrame({

"student_id": [1,2,3,4],
"name": ["messi","neha","zubin","rohit"]
  
 })

# df1.to_csv('a.csv')

df2= pd.DataFrame({

"student_id": [2,3,4,5],
"project":["ML","AI","web","app developmenrt"]

})

df2.to_csv('b.csv')