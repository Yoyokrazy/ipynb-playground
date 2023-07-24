# %pip install pa
#
#
# ndas
import logging
import os

# import re
import time

import pandas as pd
from pandas import DataFrame

data = DataFrame(
    {
        "x1": ["y", "x", "y", "x", "x", "y"],  # Construct a pandas DataFrame
        "x2": range(16, 22),
        "x3": range(1, 7),
        "x4": ["a", "b", "c", "d", "e", "f"],
        "x5": range(30, 24, -1),
    }
)
pd.array
print(data)
# import time

logging.critical("critical")

print(os.cpu_count())
# print(re)
for i in range(1, 11):
    print(i)
    print(i)
    time.sleep(0.1)
    time.sleep(0.1)
print("done!")

# BEGIN: 4f5g6h7j8k9
for i in range(10, 0, -1):
    print(i)
# END: 4f5g6h7j8k9
for i in range(1, 6):
    print(i)


import numpy as np

number = np.random.seed(123)
for i in range(1, 11):
    print(np.random.randint(1, 11))
    print(number)
