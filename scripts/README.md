
### README: Telecom xDR Dataset Preprocessing

## Project Overview

The preprocessor.py script provides utility functions to preprocess a telecom xDR dataset for analysis. The preprocessing steps include handling missing values, managing outliers, converting data units (e.g., bytes to megabytes), and removing irrelevant or redundant columns. The goal is to clean and prepare the dataset for further analysis and machine learning tasks, such as clustering and exploratory data analysis (EDA).

The load_data.py script opens a connection to postgresql and fetches the data

## Prerequisites

1. **Python 3.7+**
2. **Required Libraries:**
   - `pandas`
   - `numpy`
   - `scipy` (for statistical functions like `zscore`)

---

## Function Descriptions

### 1. `remove_columns(df, columns_to_remove)`

Removes specified columns from the DataFrame.

- **Parameters:**
  - `df`: The DataFrame from which columns will be removed.
  - `columns_to_remove`: List of column names to be removed.
- **Returns:**
  - The DataFrame with specified columns removed.

### 2. `missing_values_table(df)`

Displays the number of missing values and their percentage in each column of the DataFrame.

- **Parameters:**
  - `df`: The DataFrame to check for missing values.
- **Returns:**
  - A DataFrame listing columns with missing values, their percentage, and data types.

### 3. `handle_missing_identifiers(df, columns)`

Drops rows where missing values are found in critical identifier columns (e.g., MSISDN, IMEI).

- **Parameters:**
  - `df`: The DataFrame to process.
  - `columns`: List of identifier columns to check for missing values.
- **Returns:**
  - The DataFrame with rows containing missing identifiers removed.

### 4. `handle_missing_numerical(df, columns, threshold=65, fill_strategy='mean')`

Handles missing values in numerical columns based on a percentage threshold. Columns with missing values exceeding the threshold are dropped; otherwise, missing values are filled using the specified strategy (mean or median).

- **Parameters:**
  - `df`: The DataFrame to process.
  - `columns`: List of numerical columns to handle missing values.
  - `threshold`: Percentage threshold for dropping columns. Default is 65%.
  - `fill_strategy`: Strategy to fill missing values ('mean' or 'median').
- **Returns:**
  - The DataFrame with missing values handled in numerical columns.

### 5. `handle_missing_categorical(df, columns, fill_value='Unknown')`

Fills missing values in categorical columns with a specified value (default is 'Unknown').

- **Parameters:**
  - `df`: The DataFrame to process.
  - `columns`: List of categorical columns to handle missing values.
  - `fill_value`: Value to replace missing entries (default is 'Unknown').
- **Returns:**
  - The DataFrame with missing values filled in categorical columns.

### 6. `convert_bytes_to_megabytes(df, columns)`

Converts byte values to megabytes for the specified columns.

- **Parameters:**
  - `df`: The DataFrame to process.
  - `columns`: List of columns to convert from bytes to megabytes.
- **Returns:**
  - The DataFrame with the specified columns converted to megabytes.

### 7. `fix_outlier(df, columns)`

Replaces values exceeding the 95th percentile in numerical columns with the median value.

- **Parameters:**
  - `df`: The DataFrame to process.
  - `columns`: List of columns to fix outliers.
- **Returns:**
  - The DataFrame with outliers fixed in the specified columns.

### 8. `remove_outliers(df, columns_to_process, z_threshold=3)`

Removes rows with outliers in the specified columns based on the Z-score method. Rows with Z-scores above the threshold (default is 3) are flagged as outliers and removed.

- **Parameters:**
  - `df`: The DataFrame to process.
  - `columns_to_process`: List of columns to check for outliers.
  - `z_threshold`: Z-score threshold for determining outliers (default is 3).
- **Returns:**
  - The DataFrame with outliers removed from the specified columns.

---

## Key Points

- **Data Cleaning:** The functions handle missing data, fix outliers, and remove irrelevant columns.
- **Unit Conversion:** Data volumes can be easily converted from bytes to megabytes.
- **Outlier Handling:** Two outlier management strategies are implemented — fixing (replacing with the median) and removing (based on Z-score).

Telecom Customer Satisfaction Analysis - customer_satisfaction_app.py
Overview
This Streamlit app provides insights into telecom customer satisfaction by analyzing engagement and experience data. It allows you to calculate customer satisfaction scores, identify top satisfied customers, predict satisfaction using a regression model, perform clustering analysis, and explore handset type insights.

Features
The app consists of the following key features:

Engagement Data Analysis: Displays a summary of user engagement data, including session frequency, total duration, and traffic.
Experience Data Analysis: Displays a summary of network experience data such as TCP retransmissions, round trip time (RTT), and throughput.
Engagement Score Calculation: Calculates an engagement score for each customer based on session frequency, total session duration, and total traffic.
Experience Score Calculation: Calculates an experience score for each customer based on network performance metrics.
Satisfaction Score Calculation: Merges the engagement and experience data to compute an overall satisfaction score for each customer.
Top 10 Satisfied Customers: Lists the top 10 customers with the highest satisfaction scores.
Regression Model: Builds a linear regression model to predict customer satisfaction scores based on engagement and experience scores.
K-Means Clustering: Performs k-means clustering (k=2) on the engagement and experience scores to group customers into satisfaction clusters.
Cluster Summary: Displays the average satisfaction and experience scores for each cluster.
Handset Type Analysis: Provides insights into customer satisfaction based on handset types and identifies the top 10 handset models by satisfaction score.
