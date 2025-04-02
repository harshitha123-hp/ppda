import pandas as pd

# Load CSV file
file_path = "experience.csv"  # Change this to your actual file path
df = pd.read_csv(file_path)

# Display the last 3 rows
print("Last 3 rows of the DataFrame:")
print(df.tail(3))

# Display DataFrame information
print("\nDataFrame Information:")
print(df.info())

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())
