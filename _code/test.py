import dataclasses
import pandas as pd
import numpy as np

a = {'value': 5}

b = 'world'

c = 10

def local_fn():
    a = 5
    b = 100

    print(a)

    c = a + b

    return c

result = local_fn()

a['pie'] = 3.14

test = 'hello'

print(a)

local_fn()

# Create a large DataFrame with random data
rows, cols = 1000, 10
data = np.random.randn(rows, cols)
columns = [f'col_{i}' for i in range(cols)]

df = pd.DataFrame(data, columns=columns)

print(df)

dat = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(dat)

df
