import pandas as pd
import numpy as np

"""
    When working with tabular data, such as data stored 
    in spreadsheets or databases, Pandas is the right tool for you.
    Pandas will help you to explore, clean and process your data. 
    In Pandas, a data table is called a DataFrame.


    pandas is a Python package providing fast, flexible,
    and expressive data structures designed to make working with
    “relational” or “labeled” data both easy and intuitive. 
    It aims to be the fundamental high-level building block for doing
    practical, real world data analysis in Python. Additionally, 
    it has the broader goal of becoming the most powerful
    and flexible open source data analysis / manipulation tool available in any language.
"""

# ------------------------- Object Creation --------------------
print('------------------------- Object Creation --------------------')

print('Creating a Series by passing a list of values, letting pandas create a default integer index:')
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print()

print('Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:')
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
print()

print('Creating a DataFrame by passing a dict of objects that can be converted to series-like.')
df2 = pd.DataFrame({"A": 1.,
                    "B": pd.Timestamp('20130102'),
                    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                    "D": np.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["test", 'train', 'test', 'train']),
                    "F": 'foo'

                    })
print(df2)
print()

print('The columns of the resulting DataFrame have different dtypes.')
print(df2.dtypes)
print()

# ------------------------- Viewing Data --------------------
print('------------------------- Viewing Data --------------------')

print('Here is how to view the top and bottom rows of the frame:')
print('\t For top 3 rows :')
print(df.head(3))
print('\t For bottom 3 rows :')
print(df.tail(3))
print()

print("Display the index and columns.")
print('index:')
print(df.index)
print('columns:')
print(df.columns)
print()

"""
    DataFrame.to_numpy() gives a NumPy representation of the underlying data. Note that this can be an expensive
    operation when your DataFrame has columns with different data types, which comes down to a fundamental difference
    between pandas and NumPy: NumPy arrays have one dtype for the entire array, while pandas DataFrames
    have one dtype per column. When you call DataFrame.to_numpy(), pandas will find the NumPy dtype that
    can hold all of the dtypes in the DataFrame. This may end up being object, which requires casting every value to a
    Python object.
"""
print("To Numpy")
print(df.to_numpy())
print(df2.to_numpy())
print()

print("Show a quick summery of your data.")
print(df.describe())
print()

print("Transposing data.")
print(df.T)
print()

print("Sorting by an axis.")
print(df.sort_index(axis=1, ascending=False))
print()

print("Sorting by values of B.")
print(df.sort_values(by='B'))
print()

# ------------------------- Selection --------------------
print('------------------------- Selection --------------------')

# Getting
print('Getting.')
print()

print('Select a single column A.')
print(df['A'])
print()

print('Select via slicing.')
print(df[0:3])
print()
print(df['20130102':'20130104'])
print()

# Select by label
print('Select by label.')
print()

print('For getting a cross section using a label:')
print(df.loc[dates[0]])
print()

print('Selecting on a multi-axis by label:')
print(df.loc[:, ["A", "B"]])
print()

print('Reduction in the dimensions of the returned object:')
print(df.loc['20130102', ['A', 'B']])
print()

print('For getting a scalar value:')
print(df.loc[dates[0], 'A'])
print()

print('for getting fast access to a scalar:')
print(df.at[dates[0], 'A'])
print()

# ------------------------- Selection by position --------------------
print('------------------------- Selection by position --------------------')

print('Select via the position of passed integers:')
print(df.iloc[0], "\n")

print('By integer slice:')
print(df.iloc[3:6, 0:2], '\n')

print('By lists of integer position locations, similar to the numpy/python style:')
print(df.iloc[[1, 2, 3], [2, 3]], '\n')

print('For slicing rows explicitly:')
print(df.iloc[1:4, :], '\n')

print('For slicing column explicitly:')
print(df.iloc[:, 2:3], '\n')

print('For getting value explicitly:')
print(df.iloc[1, 1], '\n')

print('For fast access to scalar:')
print(df.iat[1, 1], '\n')

# ------------------------- Boolean indexing --------------------
print('------------------------- Boolean indexing --------------------')

print('Using a single columns\'s values to select data:')
print(df[df['A'] > 0], '\n')

print('Selecting values from a DataFrame where a boolean condition is met.')
print(df[df > 0])

df3 = df.copy()
df3['E'] = ['one', 'one', 'two', 'three', 'four', 'two']

# print(df3)
print('Using the isin method filtering:')
print(df3[df3['E'].isin(['two', 'one'])])

# ------------------------- Setting --------------------
print('------------------------- Setting --------------------')

# Setting a new column automatically aligns the data by the indexes.
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print(s1)
df['F'] = s1

# Setting value by label.
df.at[dates[0], 'A'] = 0

# Setting value by position.
df.iat[1, 1] = 0

# Setting by assigning with a numpy array.
df.loc[:, 'D'] = np.array([5] * len(df))

print(df, '\n')

# A where operation with setting.
print('A where operation with setting.')

df3 = df.copy()

df3[df3 > 0] = -df
print(df3, '\n')

# ------------------------- Mission Data --------------------
print('------------------------- Mission Data --------------------')

print('Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.')

df3 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

df3.loc[dates[0]: dates[1], 'E'] = 1
print(df3, '\n')

print('To drop any rows that have mission data.')
print(df3.dropna(how='any'), '\n')

print('Fill missing data.')
print(df3.fillna(value=5), '\n')

print('To get the boolean mask where values are nan.')
print(pd.isna(df3), '\n')

# ------------------------- Operation --------------------
print('------------------------- Operation --------------------')

# Operation general exclude missing data.

print('Performing a descriptive statistic.')
print(df.mean(), '\n')

print('Same operation on the other axis:')
print(df.mean(1), '\n')

# ------------------------- Apply --------------------
print('------------------------- Apply --------------------')

print('Applying function to the data.')
print(df.apply(np.cumsum), '\n')
print(df.apply(lambda x: x.max() - x.min()), '\n')

# ------------------------- Histogramming(uncountable mathematics) --------------------
print('------------------------- Histogramming(uncountable mathematics) --------------------')

s = pd.Series(np.random.randint(0, 7, size=10))

print(s, '\n')

# ------------------------- String Method --------------------
print('------------------------- String Method --------------------')

s = pd.Series(['A', 'B', 'C', np.nan, 'ABC', 'DEF', 'DOG', 'CAT'])
print(s.str.lower(), '\n')

# ------------------------- Merge --------------------
print('------------------------- Merge --------------------')

# Concat
df = pd.DataFrame(np.random.randn(10, 4))

print(df, '\n')

pieces = [df[:3], df[3:7], df[7:]]

print(pd.concat(pieces))

# join

left = pd.DataFrame({'KEY': ['foo', 'foo'], 'LVAL': [1, 2]})
right = pd.DataFrame({'KEY': ['foo', 'foo'], 'RVAL': [3, 4]})

print(left, '\n')
print(right, '\n')

print(pd.merge(left, right, on='KEY'), '\n')

left = pd.DataFrame({'KEY': ['foo', 'bar'], 'LVAL': [1, 2]})
right = pd.DataFrame({'KEY': ['foo', 'bar'], 'RVAL': [3, 4]})

print(left, '\n')
print(right, '\n')

print(pd.merge(left, right, on='KEY'), '\n')

df = pd.DataFrame({"A": ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'bar'],
                   "B": ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   "C": np.random.randn(8),
                   "D": np.random.randn(8)
                   })

print(df, '\n')
"""
sum of all foo and bar in C and D
"""
print('Grouping and then applying the sum() function to the resulting groups.')
print(df.groupby('A').sum(), '\n')

print('Grouping by multiple columns forms a hierarchical index, and again we can apply the sum function.')
print(df.groupby(["A", "B"]).sum(), '\n')

tuples = list(zip(['bar', 'foo', 'baz', 'baz',
                   'foo', 'foo', 'quz', 'quz'],
                  ['one', 'two', 'one', 'two',
                   'one', 'two', 'one', 'two']))

index = pd.MultiIndex.from_tuples(tuples, names=['First', 'Second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

print(df, '\n')
print('The stack method “compresses” a level in the DataFrame’s columns')

print(df.stack(), '\n')

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['a', 'b', 'c'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)

                   })

print(df, '\n')

print(pd.pivot_table(df, values='D', index=["A", "B"], columns=["C"]))
