import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

def get_value(row):
    binary_true, binary_false = 1, 0

    if row['whoAmI'] == 'human':
        row['robot'] = binary_false
        row['human'] = binary_true
    elif row['whoAmI'] == 'robot':
        row['robot'] = binary_true
        row['human'] = binary_false
    return row

data = data.apply(get_value, axis=1)
del data['whoAmI']
print(data)

