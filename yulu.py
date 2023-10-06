# -*- coding: utf-8 -*-
"""yulu.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iELcbj1rzXbWF1nHxkDm48r4jhg8ZbW
"""

import datetime
import math
import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/428/original/bike_sharing.csv?1642089089"
df_yulu = pd.read_csv(url)

# Plotting a histogram
st.subheader('Histogram: count')
plt.figure(figsize=(10,6))
sns.histplot(data=df_yulu, x='count', kde=True)
st.pyplot(plt.clf())

# Display line chart

st.write("""
            # Yulu data analyzer """)

## get data for Yulu bikes

season = st.selectbox(
    'Which season do you want to analyse?',
    ('1', '2', '3', '4'))

st.dataframe(df_yulu['season'].unique())

df=df_yulu

st.write(f"""
    ###  Season {season}'s - renting of bikes data """)

st.dataframe(df[df['season'] == 1][['casual', 'registered', 'count']])

st.write(f"""
    ### Season {season}'s - renting of bikes data""")

st.line_chart(df[df['season'] == season]['count'])