import pandas as pd

data = {'numbers1':[3, 6, 7, 1],'numbers2':[28,34,29,42], 'letters':['a', 'h', 'f', 'o']}
df = pd.DataFrame(data)

def double_number(row):
    return row["numbers1"] * 2

df["double_number"] = df.apply(double_number, axis=1)

def sum_rows(row):
    return row["numbers1"] + row["numbers2"]

df["sum_row_numbers"] = df.apply(sum_rows, axis=1)

def upper_letters(x):
    return x.upper()

print(df["letters"].apply(upper_letters))


