# -*- coding: utf-8 -*-
"""jamboree.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19TpkORzwiJyKQqinLy2JryNnpQIZwCTv#scrollTo=FlsoRbJztC_0
"""

import datetime
import math
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import statsmodels.api as sm
#from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

url = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/839/original/Jamboree_Admission.csv"
df = pd.read_csv(url)


#Remove leading and trailing white spaces in column names
df.columns=df.columns.str.strip()

st.header(f"""
                            Jamboree student admissions       
                  """)

#Check the first few rows
st.write(f"The first few rows of dataset are as follows: ")
st.write(df.head(5))

#Converting Research, SOP, LOR and Uni. Rating as categorical values

df['Research'] = df['Research'].astype('category')
df['SOP'] = df['SOP'].astype('category')
df['LOR'] = df['LOR'].astype('category')
df['University Rating']=df['University Rating'].astype('category')
cat_cols = df.select_dtypes(include=['category', 'object']).columns

# Univariate Analysis - Distribution of continuous variables
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

df_filtered=df.copy()
df_filtered.drop(['Serial No.'], axis=1, inplace=True)

st.subheader(f"""
        - Univariate Analysis.\n
        - Univariate Analysis - Histplots for numerical variables. Example: GRE Score, CGPA.\n
        """)

# Univariate Analysis - Distribution of continuous variables
num_cols = df_filtered.select_dtypes(include=['int64', 'float64']).columns
print(num_cols)
fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.set_facecolor(color = 'grey')
idx = 0
for row in range(2):
  for col in range(2):
    sns.histplot(data=df_filtered, x=num_cols[idx], ax=axis[row, col], kde=True)
    idx += 1
plt.show()
st.pyplot(fig)

st.write(f"""
    INSIGHTS:\n
        1. There is strong correlation between GRE, TOEFL and CGPA scores.\n
        2. With the histplots for numerical columns, we can say that the data is close to normal distribution.\n 
        3. GRE Score: Ranges from 290 to 340, with a mean of approximately 316.47.\n
        4. TOEFL Score: Ranges from 92 to 120, with a mean of approximately 107.19.\n
        5. CGPA: Ranges from 6.8 to 9.92, with a mean of approximately 8.58.\n
        6. Chance of Admit: Ranges from 0.34 to 0.97, with a mean of approximately 0.72.\n
        """)

st.subheader(f"""
        - Univariate Analysis.\n
        - Univariate Analysis - Boxplots for numerical variables. Example: GRE Score, CGPA.\n
        """)

# Boxplot for 'Chance of Admit' against each categorical column
fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.set_facecolor(color = 'grey')
idx = 0
for row in range(2):
  for col in range(2):
      sns.boxplot(data=df, x=cat_cols[idx], y='Chance of Admit', ax=axis[row, col])
      idx += 1
plt.grid()
plt.show()
st.pyplot(fig)

st.write(f"""
    INSIGHTS:\n
        1. There are no outliers in the independent numerical columns data viz. CGPA, GRE Score & TOEFL Score.\n
        2. There are 2 outliers in the 'Chance of Admit', but that is the target variable.\n
        3. As we can see from the boxplots, the median 'Chance of Admit' goes up with the increase in values for SOP, LOR, Research & University Rating.\n
        4. Exception: Median Chance of Admit for SOP 1.0 is greater than SOP 1.5.\n
        """)

st.subheader(f"""
        - Bivariate Analysis.\n
        - Bivariate Analysis - Scatter Plots for pairs of variables. Example: GRE Score vs CGPA.\n
        """)

ind_num_cols=['GRE Score', 'TOEFL Score', 'CGPA']
# Scatter plot for each numerical column
fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(13, 5))
fig.set_facecolor(color = 'grey')
sns.scatterplot(data=df_filtered, x=ind_num_cols[0], y=ind_num_cols[1], ax=axis[0])
sns.scatterplot(data=df_filtered, x=ind_num_cols[0], y=ind_num_cols[2], ax=axis[1])
sns.scatterplot(data=df_filtered, x=ind_num_cols[1], y=ind_num_cols[2], ax=axis[2])
plt.grid()
plt.show()
st.pyplot(fig)

#Bivariate Analysis (Relationships between important variables).
# Bivariate Analysis - Regression Plots for pairs of variables
# Example: GRE Score vs Chance of Admit

st.subheader(f"""
        - Bivariate Analysis.\n
        - Bivariate Analysis - Regplots for pairs of variables. Example: GRE Score vs Chance of Admit.\n
        """)

#Bivariate Analysis (Relationships between important variables).
# Bivariate Analysis - Regression Plots for pairs of variables
# Example: GRE Score vs Chance of Admit

ind_num_cols=['GRE Score', 'TOEFL Score', 'CGPA']
# Regplot for each numerical column
fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(13, 5))
fig.set_facecolor(color = 'grey')
idx = 0
for row in range(3):
  sns.regplot(data=df_filtered, x=ind_num_cols[idx], y='Chance of Admit', color='b', ax=axis[row])
  idx += 1
plt.grid()
plt.show()
st.pyplot(fig)

st.subheader(f"""
        - Correlation analysis using Heatmap.\n
        - Correlation analysis using pairplots.\n
        """)

# Correlation Plot using Heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = df_1.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.grid()
plt.show()
st.pyplot(fig)

# Create a pair plot
sns.pairplot(df_filtered)
# Display the plot
plt.grid()
plt.show()
st.pyplot(fig)
