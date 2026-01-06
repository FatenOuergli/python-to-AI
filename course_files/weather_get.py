import requests
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=35.864576&longitude=10.6070016&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

import pandas as pd

# Extract the daily data
daily_data = data['daily']

# Create a DataFrame
df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

# Convert date strings to datetime
df['date'] = pd.to_datetime(df['date'])
#now printing those temps (max) only above 15°C
print(df['max_temp']>15)
#now printing all the data
#head only shows the furst 5 rows
print(df.head())
print(df)

import matplotlib.pyplot as plt

# Create the plot
#marker='o' means to put a point on each date
plt.figure(figsize=(8, 4)) #8units on 4units/empty sheet at first
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Sousse Weather - Past 7 Days')
#legend for the Max temp in orange and blue the other
plt.legend()
# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()
# Save the plot
plt.savefig('weather_chart.png')
plt.show()

import os

# Create data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Save to CSV
df.to_csv('data/sousse_weather.csv', index=False)
print("Data saved to data/sousse_weather.csv")