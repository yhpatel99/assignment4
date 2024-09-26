# assignment4 : Iris Data Analysis

This assignment is going to analyze the Iris dataset by combining sepal and petal measurements, cleaning the data, and calculating various statistical metrics such as correlation matrices, averages, medians, and standard deviations for different species of irises

Data Loading:

 loading two CSV files: 
   Sepal_Data.csv  
   Petal_Data.csv

Data Merging:
  The sepal and petal data are merged into a single DataFrame using the sample_id column as the key.

Data Cleaning:
  To make sure there is accurate calculations, the data undergoes a cleaning process:

     1. Coverting to Numeric: columns that have numeric values are converted to numeric types.
     2. Dropping NaN values: rows containing NaN values are removed from the datatset to help avoid errors.

Statistical Calculations:
  The cleaned data is used to calculate the following metrics:

     1. Correlation Matrix: shows the correlations between different numeric features
     2. Averages: Mean values of numeric features grouped by species
     3. Medians: median values of numeric features grouped by species
     4. Standard deviations: standard devation values of numeric features grouped by species


Conclusion:
 This assignment creates an analysis of the Iris dataset by combining, cleaning, and calculating different statistical metrics. The results help in understanding the relationships and differences between different species of irises based on their physical measurements.
