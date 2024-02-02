# -*- coding: utf-8 -*-
"""jamboree.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19TpkORzwiJyKQqinLy2JryNnpQIZwCTv#scrollTo=FlsoRbJztC_0
"""

import datetime
import math
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

url = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/839/original/Jamboree_Admission.csv"
df_jamboree = pd.read_csv(url)
#Remove leading and trailing white spaces in column names
df_jamboree.columns=df_jamboree.columns.str.strip()
st.write(f"""
            # Jamboree students dataframe              
            """)

st.dataframe(df_jamboree.head(2))

st.write(f"""
            # ** Students admission data ** 
                                """)
## get data for Jamboree students data
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    r1 = st.selectbox(
        'What is the University Rating of the student?',
            (1, 2, 3, 4, 5))

with col2:
    r2 = st.selectbox(
        'Does the student have Research Experience?',
            (0, 1))

with col3:
    l = st.selectbox(
        'What is the strength of LOR?',
            (1.0, 1.5, 2.0, 2.5, 3.5, 4.0, 4.5, 5.0))

with col4:
    s = st.selectbox(
        'What is the strength of SOP?',
            (4.5, 4.0, 3.0, 3.5, 2.0, 5.0, 1.5, 1.0, 2.5))

st.write(f"""
    ###  CGPA, GRE Score, TOEFL Score, Chance of Admit - data for - Jamboree students: """)

df=df_jamboree[(df_jamboree['University Rating'] == r1) & (df_jamboree['Research'] == r2) & (df_jamboree['LOR'] == l) & (df_jamboree['SOP'] == s)]

#print the filtered dataframe
st.dataframe(df)

# Univariate Analysis - Distribution of continuous variables
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
print(num_cols)
fig, axis = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.set_facecolor(color = 'grey')
idx = 0
for row in range(2):
  for col in range(2):
    sns.histplot(data=df, x=num_cols[idx], ax=axis[row, col], kde=True)
    idx += 1
plt.show()
plt.show()
st.pyplot(fig)

st.write(f""" 
    INSIGHTS:
    1. .
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
    INSIGHT:
        1. There is strong correlation between GRE, TOEFL and CGPA scores.
        2. The numerical columns are normally distributed.
        """)
