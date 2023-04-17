import pandas as pd

# Load the data.csv file
df = pd.read_csv('data.csv')

# One-Hot Encoding for categorical columns
df_onehot = pd.get_dummies(df[['City', 'Ord_1']])

# Binary Encoding for binary columns
df['bin_1'] = df['bin_1'].map({'F': 0, 'M': 1})
df['bin_2'] = df['bin_2'].map({'N': 0, 'Y': 1})

# Ordinal Encoding for ordinal column
ord_mapping = {'High School': 0, 'Diploma': 1, 'Bachelors': 2, 'Masters': 3, 'PhD': 4}
df['Ord_2'] = df['Ord_2'].map(ord_mapping)

# Concatenate the encoded columns with the original data
df_encoded = pd.concat([df[['id']], df_onehot, df[['bin_1', 'bin_2', 'Ord_2', 'Target']]], axis=1)

# Save the encoded data to a new file
df_encoded.to_csv('Data_encoded.csv', index=False)