# Import script and pandas for CSV export
import scrape_wunderground as scpw
import pandas as pd

# Set station ID and date ranges as well as time interval.
# In our case, select a weather station in Chicago and retreive measurements for the whole year of 2020.
df = scpw.scrape_multidate('KILCHICA679', '2020-12-31', '2021-01-01', '5min')

# Save dataset as CSV
df.to_csv('weather_data.csv')