import pandas as pd

air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)

print(air_quality.head())

air_quality['London_mg_per_cubic'] = air_quality["station_london"] * 1.882

print(air_quality.head())

air_quality['ration_paris_antwerp']  = air_quality['station_paris'] / air_quality['station_antwerp']

print(air_quality.head())

air_quality_renamed = air_quality.reindex(columns={
                     'station_antwerp':'BETR801',
                     'station_paris': 'FR0410',
                      'station_london': 'London westminster'
})

print(air_quality_renamed.dhead())


