import pandas as pd
panda = pd.Series({
    'u' : 5,
    'v' : 6,
    'w' : 7,
    'x' : 8,
    'y' : 9,
    'z' : 10
},name='DataFrame')
print(panda[panda>7])
print(panda[(panda>7)&(panda<10)])
print(panda.mean())
print(panda.min())
print(panda.max())
print(panda.std())
panda['x'] = 2
panda[panda<7]=5
print(panda)
