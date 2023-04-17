import pandas as pd

# Load the titanic_dataset.csv file
df = pd.read_csv('titanic_dataset.csv')

# One-Hot Encoding for categorical columns
df_onehot = pd.get_dummies(df[['Sex', 'Embarked']])

# Extracting Title from Name
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Concatenate the encoded columns and new features with the original data
df_encoded = pd.concat([df[['PassengerId', 'Survived', 'Pclass', 'Age', 'Fare', 'Cabin']], df_onehot, df[['Title', 'FamilySize']]], axis=1)

# Save the encoded data to a new file
df_encoded.to_csv('Titanic_dataset_encoded.csv', index=False)