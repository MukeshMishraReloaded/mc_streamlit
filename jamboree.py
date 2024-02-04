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

st.title(f"""
            -----------------------------------      Jamboree Students admission data       -------------------------- 
            
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
    INSIGHTS:
        1. There is strong correlation between GRE, TOEFL and CGPA scores.
        2. The histplots for numerical data columns tell us that the data is almost normally distributed for each of the numerical / continious variables, which is a good sign for Linear Regression analysis.
        3. GRE Score: Ranges from 290 to 340, with a mean of approximately 316.47.
        4. TOEFL Score: Ranges from 92 to 120, with a mean of approximately 107.19.
        5. CGPA: Ranges from 6.8 to 9.92, with a mean of approximately 8.58.
        6. Chance of Admit: Ranges from 0.34 to 0.97, with a mean of approximately 0.72.
        """)

# Boxplot for 'Chance of Admit' against each categorical column
fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.set_facecolor(color = 'grey')
idx = 0
for row in range(2):
  for col in range(2):
      sns.boxplot(data=df, x=cat_cols[idx], y='Chance of Admit', ax=axis[row, col])
      idx += 1
plt.show()
plt.grid()
plt.show()
st.pyplot(fig)

st.write(f"""
    INSIGHTS:
        1. There are no outliers in the independent numerical columns data viz. CGPA, GRE Score & TOEFL Score.
        2. There are 2 outliers in the 'Chance of Admit', but that is the target variable.
        3. As we can see from the boxplots, the median 'Chance of Admit' goes up with the increase in the strength of the categorical values like SOP, LOR, University Rating & Research.
        4. Exception: Median Chance of Admit for SOP 1.0 is greater than SOP 1.5.
        """)
