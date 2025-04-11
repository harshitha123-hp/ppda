import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('5ds_salaries.csv')

# Bar plot: Experience Level vs Total Salary
plt.figure(figsize=(8, 5))
sns.barplot(x='experience_level', y='salary_in_usd', data=df, estimator=sum, errorbar=None)
plt.title('Total Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Total Salary (USD)')
plt.show()