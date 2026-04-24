import pandas as pd
df = pd.DataFrame({
    'people' :[1,2,3,4,5],
    'Food' :['Rice','Egg','Banana','vegetable','Fruit'],
    'Age' : [29,39,12,22,25]
    },index=['w','v','x','y','z'])
print(df)
print(df.columns)
print(df.shape)
print(df.size)
print(df.info())
print(df.describe())
print(df[['Food','Age']])
print(df.loc['w'])
print(df.iloc[-1])
print(df.loc['w':'z','Food'])
print(df.loc['v':'y',['people','Age']])