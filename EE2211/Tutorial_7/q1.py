import pandas as pd

# Define the data based on the given table
data = {
    'Feature 1': [0.3510, 2.1812, 0.2415, -0.1096, 0.1544],
    'Feature 2': [1.1796, 2.1068, 1.7753, 1.2747, 2.0851],
    'Feature 3': [-0.9852, 1.3766, -1.3244, -0.6316, -0.8320],
    'Target y': [0.2758, 1.4392, -0.4611, 0.6154, 1.0006]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Calculate the Pearson correlation between each feature and the target
correlation = df.corr()['Target y'][:-1]  # Exclude the target itself

# Output the correlation values
print("Pearson's correlation with Target y:\n", correlation)

# Find the feature with the highest absolute correlation value
best_feature = correlation.abs().idxmax()

print(f"The best feature to choose based on Pearson's correlation is: {best_feature}")