import pandas as pd
import matplotlib.pyplot as plt


def newline():
    print()


air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
print(air_quality.head())
newline()
# print(air_quality.plot())


# print(air_quality['station_paris'].plot())


# print(air_quality.plot.scatter(x='station_london',y='station_paris', alpha=0.5))

