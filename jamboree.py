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
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


url = "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/839/original/Jamboree_Admission.csv"
df = pd.read_csv(url)


#Remove leading and trailing white spaces in column names
df.columns=df.columns.str.strip()

st.header(f"""
                            Jamboree student admissions       
                  """)

#Print all the performance metrics for linear regression models
def get_metrics(y_true, y_pred, r, n, p, m, cols):
    """Calculate and print MAE, RMSE, R2, and Adjusted R2."""
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)
    #st.write(f'********* Regression Type: {r} *****')
    #st.write(f'MAE: {mae}')
    #st.write(f'RMSE: {rmse}')
    #st.write(f'R2: {r2}')
    #st.write(f'Adjusted R2: {adjusted_r2}')
   
    coef_df = pd.DataFrame({"Column": cols, "Coef": m.coef_})
    #st.write(f'Intercept: {m.intercept_}')
    #st.write("Coefficients: ") 
    #st.write(coef_df)
    #st.write("-"*50)
    
def train_and_test(df, regression_type='Linear', compareFeatures=False):
    """Train and test the specified regression model."""

    X = df.drop(['Chance of Admit'], axis=1)  # Assuming this as target
    y = df['Chance of Admit']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    if regression_type == 'Lasso':
      model = Lasso(alpha=0.001)
    elif regression_type == 'Ridge':
      model = Ridge(alpha=1.0)
    else:
      model = LinearRegression()
            
    model.fit(X_train, y_train)
    return model
    #Compare scaled features
    #if compareFeatures == True:
        #fig=plt.figure(figsize=(8, 6))
        #imp = pd.DataFrame(list(zip(X_test.columns,np.abs(model.coef_))),
        #           columns=['feature', 'coeff'])
        #sns.barplot(x='feature', y='coeff', data=imp)
        #plt.xticks(rotation=90)
        #plt.show()
        #st.pyplot(fig)
    #y_pred_test = model.predict(X_test)
    #y_pred_train = model.predict(X_train)
    #p_train = X_train.shape[1]
    #p_test = X_test.shape[1]
    #n_test = len(y_test)
    #n_train = len(y_train)
    #st.write(f'Performace metrics for the train dataset: ')
    #st.write(f'-------------------------------------------')
    #get_metrics(y_train, y_pred_train, regression_type, n_train, p_train, model, np.array(list(X.columns)))
    #st.write(f'Performace metrics for the test dataset: ')
    #st.write(f'-------------------------------------------')
    #get_metrics(y_test, y_pred_test, regression_type, n_test, p_test, model, np.array(list(X.columns)))

col1, col2 = st.columns(2)
with col1:
    s = st.selectbox(
        'Statement of Purpose (SOP)',
                (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0))
with col2:
    l = st.selectbox(
        'Letter of Recommendation (LOR)',
            (1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0))

col3, col4 = st.columns(2)
with col3:
    r1 = st.selectbox(
        'Research experience (No/Yes?)',
            (0, 1))
with col4:
    r2 = st.selectbox(
        'University Rating',
            (1, 2, 3, 4, 5))

# Using number_input to get a float value
c = st.number_input("Input CGPA", min_value=0.0, max_value=10.0, value=0.0, step=0.1)

# Using number_input to get a float value
g = st.number_input("Input GRE score", min_value=260.00, max_value=340.00, value=260.0, step=0.3)

# Using number_input to get a float value
t = st.number_input("Input TOEFL score", min_value=0.0, max_value=120.0, value=0.0, step=0.3)

df_1=df.copy()
df_1.drop(['Serial No.'], axis=1, inplace=True)

# Submit button
if st.button('Submit'):
    # Placeholder for processing input values
    # For example, you might calculate a score or predict admission chances here
    st.write("Values submitted successfully!")
    st.write(f"SOP: {s}, LOR: {l}, Research: {r1}, University Rating: {r2}, CGPA: {c}, GRE: {g}, TOEFL: {t}")
    
    # We now call model.predict() function here
    # and display the predicted outcome
    # Linear Regression performance metrics
    model=train_and_test(df_1, regression_type='Linear', compareFeatures=True)
    predicted_chance = model.predict([[g, t, r2, s, l, c, r1]])
    st.write(f"The chance of admit is: {predicted_chance}")
    if predicted_chance > 0.85:
        st.subheader(f"Chance of admission is quite strong!")
    elif predicted_chance > 0.7:
        st.subheader(f"Chance of admission is decent!")
    elif predicted_chance > 0.50:
        st.subheader(f"Chance of admission is weak!")
    else:
        st.subheader(f"The chance is bleak!")



st.markdown('<br><br>', unsafe_allow_html=True)  # Adds two line breaks worth of space

st.subheader(f"Exploratory data analysis")
#Check the first few rows
st.write(f"The first couple of rows of the dataset are as follows for your reference: ")
st.write(df.head(2))

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

st.subheader(f"Univariate Analysis.\n")

st.write(f"Univariate Analysis - Histplots for numerical variables. Example: GRE Score, CGPA.\n")

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

st.write(f"""
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

st.subheader(f"Bivariate Analysis.\n")

st.write(f"""
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

# Bivariate Analysis - Regression Plots for pairs of variables
# Example: GRE Score vs Chance of Admit

st.write(f"""
        - Bivariate Analysis - Regplots for pairs of variables. Example: GRE Score vs Chance of Admit.\n
        """)

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

st.write(f"""
        - Correlation analysis using Heatmap.\n
        """)

# Correlation Plot using Heatmap
fig=plt.figure(figsize=(8, 6))
correlation_matrix = df_1.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.grid()
plt.show()
st.pyplot(fig)
