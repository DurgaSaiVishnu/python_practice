# import time

# import numpy as np

# py_list = list(range(1_000_0000))
# np_array = np.arange(1_000_000)

# start = time.time()
# result = [x * 2 for x in py_list]
# print("List:", time.time() - start)

# start = time.time()
# result = np_array * 2
# print("Array:", time.time() - start)


import pandas as pd

df = pd.DataFrame([
    {"name": "Aman", "salary": 40000},
    {"name": "Riya", "salary": 65000}
])

print(f"{df.describe()}")

