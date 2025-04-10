import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\SHANTI\RVU\Programs AMinorsIDA\Activities!Datasets, 6Mcd df=null values.csv'
df = pd.read_csv(file_path)

print("Original DataFrame:")
print(df)

# Identify missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Fill missing values:
# For numeric columns – fill with mean
# For non-numeric (categorical) – fill with mode

for column in df.columns:
    if df[column].dtype == 'object':
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:
        df[column].fillna(df[column].mean(), inplace=True)

# Drop duplicate rows if any
df.drop_duplicates(inplace=True)

print("\nDataFrame after filling missing values and dropping duplicates:")
print(df)
