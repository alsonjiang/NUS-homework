#Do a scatter plot of the load_iris dataset

import pandas as pd
import matplotlib.pyplot as plt

from pandas.plotting import scatter_matrix
from sklearn.datasets import load_iris

'''
# Step 1: Load the Iris dataset
iris = load_iris()

# Step 2: Create a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
#df['species'] = iris.target

# Step 3: Create a scatter matrix
scatter_matrix(df, alpha=0.8, figsize=(20, 20), diagonal='hist', marker='o', c=df['species'], cmap='viridis')

# Display the plot
plt.suptitle('Scatter Matrix of Iris Dataset', y=1.02)
plt.show()
'''
iris = load_iris()

# Step 2: Create a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Step 3: Create a scatter matrix without coloring by species
scatter_matrix(df, alpha=0.8, figsize=(12, 12), diagonal='hist', marker='o', cmap='viridis')

# Display the plot
plt.suptitle('Scatter Matrix of Iris Dataset', y=1.02)
plt.show()