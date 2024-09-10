import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
engagement_df = pd.read_csv(r'C:\Users\Blen\OneDrive\Desktop\10Academy\Week2\notebooks\engagement_data.csv')
experience_df = pd.read_csv(r'C:\Users\Blen\OneDrive\Desktop\10Academy\Week2\notebooks\experience_data.csv')

engagement_df.rename(columns={'Customer ID': 'MSISDN/Number'}, inplace=True)
# App Title
st.title("Telecom Customer Satisfaction Analysis")

# Display raw data (optional)
st.header("Engagement Data")
st.write(engagement_df.head())

st.header("Experience Data")
st.write(experience_df.head())

# Task 4.1a - Calculate Engagement Score
st.subheader("Task 4.1a: Calculate Engagement Score")
engagement_clusters_df = engagement_df.groupby('Engagement Cluster')[['Session Frequency', 'Total Duration (ms)', 'Total Traffic (Bytes)']].mean()
engagement_clusters = engagement_clusters_df.values

def calculate_engagement_score(row):
    return euclidean_distances([row], [engagement_clusters[0]])[0][0]

engagement_df['engagement_score'] = engagement_df.apply(
    lambda row: calculate_engagement_score(row[['Session Frequency', 'Total Duration (ms)', 'Total Traffic (Bytes)']]), axis=1)

st.write(engagement_df[['MSISDN/Number', 'engagement_score']].head())

# Task 4.1b - Calculate Experience Score
st.subheader("Task 4.1b: Calculate Experience Score")
experience_clusters_df = experience_df.groupby('Experience Cluster')[['Avg TCP Retransmission (Bytes)', 'Avg RTT (ms)', 'Avg Throughput (kbps)']].mean()
experience_clusters = experience_clusters_df.values

def calculate_experience_score(row):
    return euclidean_distances([row], [experience_clusters[0]])[0][0]

experience_df['experience_score'] = experience_df.apply(
    lambda row: calculate_experience_score(row[['Avg TCP Retransmission (Bytes)', 'Avg RTT (ms)', 'Avg Throughput (kbps)']]), axis=1)

st.write(experience_df[['MSISDN/Number', 'experience_score']].head())

# Task 4.2 - Calculate Satisfaction Score
st.subheader("Task 4.2: Satisfaction Score & Top 10 Customers")
df_merged = pd.merge(engagement_df[['MSISDN/Number','Handset Type','engagement_score']],
                     experience_df[['MSISDN/Number','experience_score']],
                     on='MSISDN/Number',
                     how='inner')

df_merged['satisfaction_score'] = df_merged[['engagement_score', 'experience_score']].mean(axis=1)

top_10_satisfied = df_merged.nlargest(10, 'satisfaction_score')
st.write("Top 10 Satisfied Customers:")
st.write(top_10_satisfied[['MSISDN/Number', 'satisfaction_score']])

# Task 4.3 - Build a Regression Model to Predict Satisfaction Score
st.subheader("Task 4.3: Predicting Satisfaction Score")

features = df_merged[['engagement_score', 'experience_score']]
target = df_merged['satisfaction_score']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
st.write(f"Model R^2: {model.score(X_test, y_test):.2f}")

# Task 4.4 - K-Means Clustering (k=2)
st.subheader("Task 4.4: K-Means Clustering on Engagement & Experience Score (k=2)")
kmeans_satisfaction = KMeans(n_clusters=2, random_state=42)
df_merged['satisfaction_cluster'] = kmeans_satisfaction.fit_predict(df_merged[['engagement_score', 'experience_score']])

st.write("Cluster Assignment:")
st.write(df_merged[['MSISDN/Number', 'satisfaction_cluster']].head())

# Task 4.5 - Aggregate Average Satisfaction & Experience Score per Cluster
st.subheader("Task 4.5: Cluster Summary")
cluster_aggregation = df_merged.groupby('satisfaction_cluster').agg({
    'satisfaction_score': 'mean',
    'experience_score': 'mean',
    'MSISDN/Number': 'count'
}).rename(columns = {'MSISDN/Number': 'Number of Users'}).reset_index()

st.write(cluster_aggregation)

# Visualization for Clustering
st.subheader("Visualization: Engagement & Experience Clustering")

plt.figure(figsize=(10,6))
sns.scatterplot(
    x='engagement_score', y='experience_score',
    hue='satisfaction_cluster',
    palette='Set1',
    data=df_merged
)
plt.title('Clusters based on Engagement and Experience Scores')
plt.xlabel('Engagement Score')
plt.ylabel('Experience Score')
st.pyplot(plt)

# Task 4.6 - Handset Type Analysis
st.subheader("Task 4.6: Handset Type Analysis")

handset_grouped = df_merged.groupby('Handset Type')['satisfaction_score'].mean().reset_index()
handset_grouped = handset_grouped.sort_values(by='satisfaction_score', ascending=False).head(10)

st.write("Top 10 Handsets by Satisfaction Score:")
st.write(handset_grouped)

plt.figure(figsize=(12,6))
sns.barplot(x='Handset Type', y='satisfaction_score', data=handset_grouped)
plt.title('Top 10 Handsets by Satisfaction Score')
plt.xticks(rotation=45)
plt.ylabel('Satisfaction Score')
plt.xlabel('Handset Type')
st.pyplot(plt)
