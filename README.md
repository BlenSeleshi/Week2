### README for Telecom Customer Experience and Satisfaction Analysis Project

---

#### **Project Overview**

This project aims to analyze customer experience, engagement, and satisfaction using a telecom xDR (Call Detail Record) dataset. The analysis is divided into four main tasks, each focusing on distinct but interrelated aspects of customer behavior, network performance, and overall satisfaction.

---

### **Tasks Overview**

#### **Task 1: User Overview Analysis**

- **Objective**: Understand overall user behavior by analyzing key metrics like session frequency, session duration, and total traffic per user.
- **Key Activities**:
  - Aggregated user data based on unique identifier columns such as IMEI, IMSI, and MSISDN.
  - Identified top 10 customers based on various engagement metrics (session frequency, duration, total traffic).
  - Used k-means clustering to segment users based on engagement levels.
  - Analyzed the engagement patterns and identified potential high-value customers.
- **Deliverables**:
  - Top 10 most engaged users.
  - Engagement clustering and summary statistics.
  - Recommendations for improving user engagement.

#### **Task 2: User Engagement Analysis**

- **Objective**: Provide in-depth analysis of user engagement metrics across various applications and services.
- **Key Activities**:
  - Normalized engagement metrics to classify users into clusters (k=3) using k-means clustering.
  - Aggregated traffic per application (e.g., Social Media, YouTube, Netflix) to identify top users for each application.
  - Visualized the top 3 most-used applications to understand user preferences.
  - Determined optimal engagement clusters and provided insights on how to improve user engagement for lower-performing segments.
- **Deliverables**:
  - Application-specific traffic analysis.
  - Engagement cluster summaries.
  - Visual representation of top applications and engagement clusters.

#### **Task 3: User Experience Analysis**

- **Objective**: Analyze network performance metrics (TCP Retransmission, RTT, Throughput) and assess their impact on user experience.
- **Key Activities**:
  - Aggregated network performance data per user based on customer MSISDN/Number.
  - Computed top, bottom, and most frequent values for TCP retransmission, RTT, and Throughput.
  - Performed distribution analysis of average throughput and TCP retransmission per handset type.
  - Applied k-means clustering (k=3) to group users based on network experience.
- **Deliverables**:
  - Summary of top, bottom, and frequent network performance metrics.
  - Visual representation of network performance per handset type.
  - Cluster analysis and user segmentation based on experience metrics.

#### **Task 4: Satisfaction Analysis**

- **Objective**: Calculate overall customer satisfaction by combining user engagement and experience scores and building a predictive model.
- **Key Activities**:
  - Calculated engagement scores using euclidean distances from the engagement cluster centroids.
  - Calculated experience scores similarly based on experience cluster centroids.
  - Combined engagement and experience scores to compute a satisfaction score for each user.
  - Built a regression model to predict satisfaction based on engagement and experience scores.
  - Applied k-means clustering (k=2) to segment users based on satisfaction and analyzed the clusters for insights.
  - Exported the results to a PostgreSQL database for further reporting and integration.
- **Deliverables**:
  - Top 10 satisfied customers based on the calculated satisfaction score.
  - Regression model predicting satisfaction.
  - Satisfaction clustering summary.
  - Database integration for customer satisfaction insights.

---

### **Company Objectives Addressed**

1. **Improve Customer Satisfaction**: By analyzing user experience and engagement data, the company can identify areas of improvement in the network and user services, directly enhancing customer satisfaction.
2. **Target High-Value Customers**: The project identifies top-engaged and top-satisfied customers, enabling the company to design targeted retention campaigns for high-value users.

3. **Enhance Network Performance**: With detailed analysis of network performance metrics like TCP retransmission and throughput, the company can focus on optimizing network performance to minimize customer complaints and improve overall service quality.

4. **Data-Driven Decision Making**: The insights provided by clustering and regression analysis allow the company to make informed decisions regarding service improvements, customer engagement strategies, and resource allocation.

---

### **Requirements**

- **Libraries**:
  - Pandas, NumPy, Matplotlib, Seaborn
  - Scikit-learn (for clustering and regression)
  - SQLAlchemy and Psycopg2 (for database integration)
- **Data**: Telecom xDR dataset, including customer session metrics, network performance data, and handset information.

### **How to Run the Analysis**

1. Load the datasets (`preprocessed_telecom_xdr_data.csv`, `engagement_data.csv`, and `experience_data.csv`).
2. Execute each task sequentially:
   - Task 1: User Overview Analysis
   - Task 2: User Engagement Analysis
   - Task 3: User Experience Analysis
   - Task 4: Satisfaction Analysis
3. For Task 4, ensure that the PostgreSQL database connection is correctly configured in the environment variables.
4. After execution, review the generated insights, visualizations, and exported data for further use.

### **Conclusion**

## This project provides a comprehensive framework for understanding telecom customer behavior by merging engagement and experience metrics into actionable insights.
