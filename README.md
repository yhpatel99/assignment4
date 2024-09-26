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

     1. Conversion to Numeric: Columns that should contain numeric values (petal_length, petal_width, sepal_length, sepal_width) are converted to numeric types.  
     2. Dropping NaN Values: Rows containing NaN values are removed from the dataset to avoid errors.

Statistical Calculations:
  The cleaned data is used to calculate the following metrics:

    1. Correlation Matrix: Shows the correlation between different numeric features.
    2.Averages: Mean values of numeric features grouped by species.
    3.Medians: Median values of numeric features grouped by species.
    4.Standard Deviations: Standard deviation values of numeric features grouped by species.
