import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\Users\encar\Downloads\zomato.csv',encoding='latin-1')
# print(df.head())
# print(df.columns)
# print(df.info())
# print(df.describe())

print(df.isnull().sum())

# print([features for features in df.columns if df[features].insull().sum()>0])

(sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap= 'viridis'))
                                          
                                



