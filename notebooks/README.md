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

Task 3: User Experience Analysis
Objective:
Task 3 focuses on evaluating user experience through metrics such as TCP retransmission, Round Trip Time (RTT), and Throughput. Users are clustered based on these metrics to understand different experience levels.

Steps:
3.1 Aggregate Per Customer:
Dataset: Telecom xDR data.
Columns Used:
MSISDN/Number (Customer ID).
Handset Type.
Network metrics: TCP DL Retrans. Vol (Bytes), TCP UL Retrans. Vol (Bytes), Avg RTT DL (ms), Avg RTT UL (ms), Avg Bearer TP DL (kbps), and Avg Bearer TP UL (kbps).
Aggregations:
Mean TCP Retransmission (TCP DL Retrans. Vol (Bytes) + TCP UL Retrans. Vol (Bytes)).
Mean RTT (Avg RTT DL (ms) + Avg RTT UL (ms)).
Mean Throughput (Avg Bearer TP DL (kbps) + Avg Bearer TP UL (kbps)).
3.2 Compute & List Top, Bottom, and Most Frequent Values:
Top 10, Bottom 10, and Most Frequent values were computed for:
Avg TCP Retransmission (Bytes)
Avg RTT (ms)
Avg Throughput (kbps)
3.3 Compute & Report Distributions:
Distribution of Average Throughput and TCP Retransmission per Handset Type:
Visualized the average throughput and retransmission for different handset types using bar plots.
3.4 K-Means Clustering:
Applied K-Means Clustering (k=3) to segment customers based on:
Avg TCP Retransmission (Bytes)
Avg RTT (ms)
Avg Throughput (kbps)
Visualized clusters based on throughput and RTT.

Task 4: Satisfaction Analysis
Objective:
Task 4 involves calculating customer satisfaction based on their engagement and experience, followed by building a regression model and exporting results to a PostgreSQL database.

Steps:
4.1 Calculate Engagement & Experience Scores:
Engagement Score: Calculated using session frequency, session duration, and total traffic.
Experience Score: Calculated using average TCP retransmission, RTT, and throughput.
Euclidean Distance method was used to compute both scores based on cluster centers.
4.2 Calculate Satisfaction Score:
Satisfaction score is computed as the average of the engagement and experience scores.
Top 10 most satisfied customers were identified based on the satisfaction score.
4.3 Build a Regression Model:
A Linear Regression Model was built to predict satisfaction scores using engagement and experience scores.
Data was split into training and test sets, and the model was evaluated using the R-squared score.
4.4 K-Means Clustering on Satisfaction:
Performed K-Means Clustering (k=2) on engagement and experience scores to segment customers.
Analyzed the cluster assignments.
4.5 Aggregate Satisfaction & Experience Score per Cluster:
Aggregated the average satisfaction and experience scores per cluster and reported the number of users in each cluster.

Database Integration:
The results, including MSISDN/Number, handset type, engagement score, experience score, and satisfaction score, were exported to a PostgreSQL database using SQLAlchemy.
A verification query was executed to ensure the data was correctly inserted into the customer_satisfaction table.
