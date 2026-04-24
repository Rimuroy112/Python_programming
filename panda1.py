import numpy as np
import pandas as pd
panda = pd.Series([1,2,3,4,5])
panda.name = 'Robotics'
panda.index = [
    'a',
    'b',
    'c',
    'd',
    'e',
]
print(panda.dtype)
print(panda.values)
print(type(panda.values))
print(panda)
print(panda['d'])
panda2 = pd.Series({
    'x':1,
    'y':2,
    'z':3,
    'w':4,
    'k':5},name='RobohuntersBRUR')
print(panda2)
print(panda2['y'])
print(panda2.iloc[2])
print(panda2[['w','k']])
print(panda2['x':'k'])
