import pandas as pd

# Load data
sepal_data = pd.read_csv('Sepal_Data.csv')
petal_data = pd.read_csv('Petal_Data.csv')

# Combine datasets
combined_data = pd.merge(sepal_data, petal_data, on='sample_id')

# Rename one of the species columns to 'species' and drop the other
combined_data['species'] = combined_data['species_x']
combined_data = combined_data.drop(columns=['species_x', 'species_y'])

# Data cleaning: Remove rows with non-numeric values in numeric columns
numeric_columns = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width']
for column in numeric_columns:
    combined_data[column] = pd.to_numeric(combined_data[column], errors='coerce')

# Drop rows with NaN values (resulting from conversion errors)
combined_data = combined_data.dropna()

print("Cleaned Data:\n", combined_data)

# make sure only numeric columns are used 
numeric_data = combined_data[numeric_columns]

# Calculate correlations
correlation_matrix = numeric_data.corr()

# Calculate averages, medians, and standard deviations
# only numeric columns are used for groupby calculations
grouped_data = combined_data.groupby('species')[numeric_columns]

averages = grouped_data.mean()
medians = grouped_data.median()
std_devs = grouped_data.std()

# Display results
print("Correlation Matrix:\n", correlation_matrix)
print("\nAverages:\n", averages)
print("\nMedians:\n", medians)
print("\nStandard Deviations:\n", std_devs)

#Versicolor and Virginica are more similar to each other compared to Setosa. This is because of their closer averages and standard deviations in petal length and petal width.
#Setosa is the least similar to both Versicolor and Virginica, becasue itWrite a ReadMe file explaining the purpose of your project. Include explanations for your class design and implementation, as well as each class attribute, method, and any limitations that you added. has significantly different averages and lower standard deviations in all measurements.