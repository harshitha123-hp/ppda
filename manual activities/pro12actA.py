import seaborn as sns

import matplotlib.pyplot as plt

# Visualizing outliers in the 'Weight_kg' column using matplotlib
plt.figure(figsize=(8, 6))
plt.boxplot(data['Weight_kg'], vert=False, patch_artist=True, notch=True, showmeans=True)
plt.title('Box Plot of Weight (kg) - Matplotlib')
plt.xlabel('Weight (kg)')
plt.show()

# Visualizing outliers in the 'Weight_kg' column using seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(x=data['Weight_kg'])
plt.title('Box Plot of Weight (kg) - Seaborn')
plt.xlabel('Weight (kg)')
plt.show()