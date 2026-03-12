#!/usr/bin/env python
# coding: utf-8

# In[16]:


from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib as jb


# In[17]:


model = jb.load("LogisticRegression.pkl")


# In[18]:


app = FastAPI(title="Telecom Churn Prediction API")


# In[19]:


class CustomerData(BaseModel):
    AccountWeeks: int
    ContractRenewal: int
    DataPlan: int
    DataUsage: float
    CustServCalls: int
    DayMins: float
    DayCalls: int
    MonthlyCharge: float
    OverageFee: float
    RoamMins: float


# In[20]:


@app.get("/")
def home():
    return {"message": "Telecom Churn Prediction API running"}


# In[21]:


@app.post("/predict")
def predict(data: CustomerData):

    df = pd.DataFrame({
        "AccountWeeks": [data.AccountWeeks],
        "ContractRenewal": [data.ContractRenewal],
        "DataPlan": [data.DataPlan],
        "DataUsage": [data.DataUsage],
        "CustServCalls": [data.CustServCalls],
        "DayMins": [data.DayMins],
        "DayCalls": [data.DayCalls],
        "MonthlyCharge": [data.MonthlyCharge],
        "OverageFee": [data.OverageFee],
        "RoamMins": [data.RoamMins]
    })
    prediction = model.predict(df)

    return {"prediction": int(prediction[0])}


# In[ ]:




