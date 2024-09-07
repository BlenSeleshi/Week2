### README: Telecom xDR Data Analysis (Task 1 & Task 2)

## Prerequisites

1. **Python 3.7+**
2. **Required Libraries:**
   - pandas
   - numpy
   - matplotlib
   - seaborn
   - scikit-learn (for KMeans clustering)
   - plotly (for interactive visualizations)
   - Jupyter Notebook (for running the notebooks)

## Task 1: User Overview Analysis

### Objective:

To gain insights into user behavior by analyzing handset usage and aggregating session data across various applications.

### Sub-tasks:

1. **Identify Top Handsets & Manufacturers**:

   - Identify the top 10 handsets used by customers.
   - Identify the top 3 handset manufacturers and the top 5 handsets for each of them.

2. **Aggregate User Session Data**:

   - Aggregate per user the number of xDR sessions, total session duration, and total download/upload data for each application (e.g., Social Media, YouTube, Netflix, etc.).
   - Track total data volume per application per user.

3. **Exploratory Data Analysis (EDA)**:

   - Perform univariate and bivariate analysis to understand the distribution and relationships between key metrics.
   - Handle missing values and outliers using appropriate techniques (e.g., replacing missing values with means).

4. **Recommendations**:
   - Provide recommendations based on the findings from the analysis for the marketing teams.

### Files:

- `Task_1.ipynb`: This notebook contains the full implementation of Task 1, including data aggregation, EDA, and recommendations.

### How to Run Task 1:

1. Load the dataset using pandas.
2. Run the data preprocessing section to clean and prepare the data.
3. Execute each section in the notebook to perform the analyses.
4. The final output will display insights, visualizations, and recommendations.

---

## Task 2: User Engagement Analysis

### Objective:

To analyze user engagement based on session frequency, duration, and data traffic per application, and to group users into clusters based on their engagement levels.

### Sub-tasks:

1. **Aggregate User Engagement Metrics**:

   - Aggregate metrics (session frequency, session duration, total download/upload data) per user (MSISDN).
   - Report the top 10 customers for each engagement metric.

2. **Normalize and Cluster Users**:

   - Normalize engagement metrics (e.g., Min-Max scaling) and apply the K-Means clustering algorithm to group users into three engagement clusters (k=3).
   - Use the elbow method to find the optimal value of `k`.

3. **Cluster Analysis**:

   - Compute the minimum, maximum, average, and total non-normalized metrics for each cluster.
   - Visualize the results and interpret the findings.

4. **Application Traffic**:
   - Aggregate total traffic per application per user.
   - Derive the top 10 most engaged users for each application.
   - Plot the top 3 most-used applications.

### Files:

- `Task_2.ipynb`: This notebook contains the full implementation of Task 2, including customer segmentation, k-means clustering, and visualizations.

### How to Run Task 2:

1. Load the dataset using pandas.
2. Run the data preprocessing section to clean and prepare the data.
3. Execute each section to perform engagement analysis and clustering.
4. The final output will include visualizations of the top users per engagement metric and the clustered user segments.

---

## How to Use the Notebooks

1. Clone this repository and ensure you have the necessary Python libraries installed.
2. Open each notebook (`Task1_User_Overview.ipynb` and `Task2_User_Engagement.ipynb`) in Jupyter Notebook or any Python IDE that supports notebooks.
3. Follow the instructions within the notebooks to execute each section.
4. Visualizations will be displayed inline within the notebook, and key insights will be printed as outputs.

## Key Insights

- **User Overview Analysis** (Task 1) identified the top handset manufacturers, key applications contributing to data usage, and suggestions for targeting marketing efforts.
- **User Engagement Analysis** (Task 2) classified users into distinct clusters based on engagement levels, helping the business to optimize resource allocation for high-engagement users.
