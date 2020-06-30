import sqlite3
import pandas as pd
from matplotlib import pyplot

cnx = sqlite3.connect("src/co2/db.sqlite3")
df = pd.read_sql_query("select co2_rate, datetime from co2_france_co2emission", cnx)
df['datetime'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H:%M:%S")
df.set_index('datetime', inplace=True)
df.index = pd.to_datetime(df.index)
df_interpol = df.resample('h').mean()
df_interpol['co2_rate'] = df_interpol['co2_rate'].interpolate()
print("Data median (by trim):", df.resample('3M', label='right')['co2_rate'].median())
print("Interpolated data median (by trim):", df_interpol.resample('3M', label='right')['co2_rate'].median())
print("Data mean (working days):", df.resample('5B')['co2_rate'].mean())
print("Interpolated data mean (working days):", df_interpol.resample('5B')['co2_rate'].mean())
print("Data mean (Sun):", df.resample('W-Sun')['co2_rate'].mean())
print("Data mean (Sat):", df.resample('W-Sat')['co2_rate'].mean())
print("Data mean (Sun):", df.resample('W-Sun')['co2_rate'].mean())
print("Data mean (Sat):", df.resample('W-Sat')['co2_rate'].mean())

csv_df = pd.read_csv("https://frama.link/8Hne12Q2", delimiter=";", header=0, index_col=4, parse_dates=True, squeeze=True)
print(csv_df)
df_co2_production = csv_df['Consommation (MW)']*1000*csv_df['Taux de CO2 (g/kWh)']

print("Production CO2 (g/h):", df_co2_production)


ax = df.plot()
df_interpol.plot(ax=ax)
pyplot.show()


