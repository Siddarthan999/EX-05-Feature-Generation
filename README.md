# EX-05-Feature-Generation

# AIM:

To read the given data and perform Feature Generation process and save the data to a file.

# Explanation:

Feature Generation (also known as feature construction, feature extraction or feature engineering) is the process of transforming features into new features that better relate to the target.

# ALGORITHM:

# STEP 1

Read the given Data

# STEP 2

Clean the Data Set using Data Cleaning Process

# STEP 3

Apply Feature Generation techniques to all the feature of the data set

# STEP 4

Save the data to the file

# PROGRAM:

# FOR “data.csv”

    import pandas as pd

    #Load the data.csv file

    df = pd.read_csv('data.csv')

    #One-Hot Encoding for categorical columns

    df_onehot = pd.get_dummies(df[['City', 'Ord_1']])

    #Binary Encoding for binary columns

    df['bin_1'] = df['bin_1'].map({'F': 0, 'M': 1})

    df['bin_2'] = df['bin_2'].map({'N': 0, 'Y': 1})

    #Ordinal Encoding for ordinal column

    ord_mapping = {'High School': 0, 'Diploma': 1, 'Bachelors': 2, 'Masters': 3, 'PhD': 4}

    df['Ord_2'] = df['Ord_2'].map(ord_mapping)

    #Concatenate the encoded columns with the original data

    df_encoded = pd.concat([df[['id']], df_onehot, df[['bin_1', 'bin_2', 'Ord_2', 'Target']]], axis=1)

    #Save the encoded data to a new file

    df_encoded.to_csv('Data_encoded.csv', index=False)

# OUTPUT
![image](https://user-images.githubusercontent.com/91734840/232391285-79bf654c-a3c2-455c-b298-44bf89d145f3.png)

# FOR “Encoding_Data.csv”

    import pandas as pd

    #Load the encoding.csv file

    df = pd.read_csv('Encoding_Data.csv')

    #One-Hot Encoding for categorical columns

    df_onehot = pd.get_dummies(df[['bin_1', 'bin_2', 'nom_0', 'ord_2']])

    #Binary Encoding for binary columns

    df['bin_1'] = df['bin_1'].map({'F': 0, 'T': 1})

    df['bin_2'] = df['bin_2'].map({'N': 0, 'Y': 1})

    #Ordinal Encoding for ordinal column

    ord_mapping = {'Cold': 0, 'Warm': 1, 'Hot': 2}

    df['ord_2'] = df['ord_2'].map(ord_mapping)

    #Concatenate the encoded columns with the original data

    df_encoded = pd.concat([df[['id']], df_onehot, df[['bin_1', 'bin_2', 'ord_2']]], axis=1)

    #Save the encoded data to a new file

    df_encoded.to_csv('Encoding_encoded.csv', index=False)

    # OUTPUT
    ![image](https://user-images.githubusercontent.com/91734840/232391362-a7e15c8f-0203-4033-9587-e6695f1d3e75.png)

    # FOR “titanic_dataset.csv”

    import pandas as pd

    #Load the titanic_dataset.csv file

    df = pd.read_csv('titanic_dataset.csv')

    #One-Hot Encoding for categorical columns

    df_onehot = pd.get_dummies(df[['Sex', 'Embarked']])

    #Extracting Title from Name

    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

    #Family Size

    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    #Concatenate the encoded columns and new features with the original data

    df_encoded = pd.concat([df[['PassengerId', 'Survived', 'Pclass', 'Age', 'Fare', 'Cabin']], df_onehot, df[['Title', 'FamilySize']]], axis=1)

    #Save the encoded data to a new file

    df_encoded.to_csv('Titanic_dataset_encoded.csv', index=False)

# OUTPUT
![image](https://user-images.githubusercontent.com/91734840/232391404-a10286cf-fc7d-4636-b365-722a35b52e91.png)

# RESULT:

Thus, to read the given data and perform Feature Generation process and save the data to a file has been successfully performed.
