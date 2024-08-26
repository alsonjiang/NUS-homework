import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('EE2211/pima-indians-diabetes.data.csv', header=None)

#a. summary statistics
print('##############PART A')
print(df.describe())
print('##############PART A')

#b. count no. of 0s in cols 1-5
zero_counts = (df.iloc[:, 0:6] == 0).sum(axis=0)
print('##############PART B')
print(zero_counts)
print('##############PART B')

#c. replace 0s with NaN
df.replace(0, np.nan, inplace=True)
#df.fillna("NaN", inplace=True)
df.to_csv('EE2211/modified_pima_indians.csv', index=False, header=False)
print("Modified DataFrame has been saved to 'modified_file.csv'.")

