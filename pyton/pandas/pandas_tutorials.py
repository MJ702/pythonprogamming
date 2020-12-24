import pandas as pd


def newline():
    print()


titanic = pd.read_csv('titanic.csv')

print(titanic.head())
newline()

ages = titanic['Age']
print(ages.head())
newline()
print(titanic['Age'].shape)
newline()

ages_sex = titanic[["Age", 'Sex']]
print(ages_sex.head())
newline()
print(titanic[['Age', "Sex"]].shape)
newline()

above_35 = titanic[titanic['Age'] > 35]
print(above_35)
newline()
print(titanic[titanic["Age"] > 35].shape)
newline()

class_23 = titanic[titanic['Pclass'].isin([2, 3])]
print(class_23)
newline()

age_no_nan = titanic[titanic['Age'].notna()]
print(age_no_nan)
newline()
print(age_no_nan.shape)
newline()

"""When using loc/iloc, the
part before the comma is the rows you want, and the part after the comma is the columns you want to select."""
adult_name = titanic.loc[titanic['Age'] > 35, "Name"]
print(adult_name)
newline()

print(titanic.iloc[9:25, 2:5])
newline()

titanic.iloc[0:3, 3] = 'anonymous'
print(titanic.head())
newline()

