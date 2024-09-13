#Plot the educational expenditure over the years

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('EE2211/government-expenditure-on-education.csv')

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df['year'], df['recurrent_expenditure_total'], marker='o')
plt.title('Government Expenditure on Education Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Expenditure on Education (SGD)')
plt.grid(True)
plt.show()