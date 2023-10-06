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

st.write("""
            # Yulu bikes data """)

## get data for Yulu bikes
col1, col2 = st.columns(2)
with col1:
    s = st.selectbox(
        'Which season do you want to select?',
            (1, 2, 3, 4))
with col2:
    w = st.selectbox(
        'Which weather do you want to select?',
            (1, 2, 3, 4))
st.write(f"""
    ###  Season {s}'s and weather {w}'s data for - renting of Yulu bikes: """)

st.dataframe( df_yulu[ (df_yulu['season'] == s) & (df_yulu['weather'] == w) ][['casual', 'registered', 'count']] )
