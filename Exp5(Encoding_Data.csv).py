import pandas as pd

# Load the encoding.csv file
df = pd.read_csv('Encoding_Data.csv')

# One-Hot Encoding for categorical columns
df_onehot = pd.get_dummies(df[['bin_1', 'bin_2', 'nom_0', 'ord_2']])

# Binary Encoding for binary columns
df['bin_1'] = df['bin_1'].map({'F': 0, 'T': 1})
df['bin_2'] = df['bin_2'].map({'N': 0, 'Y': 1})

# Ordinal Encoding for ordinal column
ord_mapping = {'Cold': 0, 'Warm': 1, 'Hot': 2}
df['ord_2'] = df['ord_2'].map(ord_mapping)

# Concatenate the encoded columns with the original data
df_encoded = pd.concat([df[['id']], df_onehot, df[['bin_1', 'bin_2', 'ord_2']]], axis=1)

# Save the encoded data to a new file
df_encoded.to_csv('Encoding_encoded.csv', index=False)