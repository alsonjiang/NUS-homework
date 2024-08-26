#Extract and plot the number of Omnibuses, 
#Excursion buses and Private buses over the years as shown below

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('EE2211/AnnualMotorVehiclePopulationbyVehicleType.csv')

vehicles = ['Omnibuses','Excursion buses','Private buses']
filtered_df = df[df['type'].isin(vehicles)]

plt.figure(figsize=(10, 6))

for vehicle in vehicles:
    subset = filtered_df[filtered_df['type'] == vehicle]
    plt.plot(subset['year'], subset['number'], marker='o', label=vehicle)

plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.title('Number of Vehicles by Type Over the Years')
plt.legend()

plt.show()