import pandas as pd

# Load the CSV file
file_path = '2Salary.csv'  # Adjust the path if needed
df = pd.read_csv(file_path)

print("Loaded Data:")
print(df.head())

# Assuming the salary column is named 'Salary'
# If it has a different name, you can print df.columns to check

salary_col = 'Salary'

print("\n--- Central Tendency Measures ---")
print(f"Mean: {df[salary_col].mean()}")
print(f"Median: {df[salary_col].median()}")
print(f"Mode: {df[salary_col].mode()[0]}")

print("\n--- Dispersion Measures ---")
print(f"Standard Deviation: {df[salary_col].std()}")
print(f"Variance: {df[salary_col].var()}")
print(f"Minimum: {df[salary_col].min()}")
print(f"Maximum: {df[salary_col].max()}")
print(f"Range: {df[salary_col].max() - df[salary_col].min()}")

# Interquartile Range (IQR)
Q1 = df[salary_col].quantile(0.25)
Q3 = df[salary_col].quantile(0.75)
IQR = Q3 - Q1
print(f"IQR (Q3 - Q1): {IQR}")
