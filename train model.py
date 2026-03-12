#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib as jb


# In[5]:


df = pd.read_csv("telecom_churn.csv")


# In[9]:


df.head()


# In[10]:


x = df.drop(['Churn'], axis=1)
y = df['Churn']


# In[11]:


numerical_cols = x.select_dtypes(include=['int64','float64']).columns.tolist()


# In[12]:


categorical_cols = x.select_dtypes(include=['object']).columns.tolist()


# In[13]:


numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])


# In[14]:


categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])


# In[15]:


preprocessor = ColumnTransformer(transformers=[
    ('num',numerical_transformer,numerical_cols ),
    ('cate',categorical_transformer,categorical_cols )
])


# In[16]:


X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)


# In[18]:


model = Pipeline(steps=[
    ('pre',preprocessor ),('log',LogisticRegression(max_iter=1000))
])


# In[19]:


model.fit(X_train,y_train)


# In[21]:


y_pred = model.predict(X_test)
print(f'{classification_report(y_test,y_pred,zero_division = 0)}')


# In[26]:


jb.dump(model,'LogisticRegression.pkl')

