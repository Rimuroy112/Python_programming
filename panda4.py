import pandas as pd
df = pd.DataFrame({ 'population' : [10,20,30],
                    'GDP' : [2.3,3.5,4.2],
                    'Surface' : [1,5,7],
                    'continent' : ['America','London','Sydney']
                  },columns = ['population','GDP','Surface','continent'])

print(df.iloc[0:2,3])
print(df.loc[df['GDP']>3,'GDP'])
print(df.loc[(df['GDP']>2) & (df['GDP']<4),['population','continent']])
print(df.drop('Surface', axis=1))
