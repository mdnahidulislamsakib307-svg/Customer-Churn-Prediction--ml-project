#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
import requests

st.title("Customer Churn Prediction App")

AccountWeeks = st.number_input("Account Weeks")

ContractRenewal = st.selectbox(
    "Contract Renewal",
    [0,1]
)

DataPlan = st.selectbox(
    "Data Plan",
    [0,1]
)

DataUsage = st.number_input("Data Usage")
CustServCalls = st.number_input("Customer Service Calls")
DayMins = st.number_input("Day Minutes")
DayCalls = st.number_input("Day Calls")
MonthlyCharge = st.number_input("Monthly Charge")
OverageFee = st.number_input("Overage Fee")
RoamMins = st.number_input("Roaming Minutes")

if st.button("Predict"):

    data = {
        "AccountWeeks": AccountWeeks,
        "ContractRenewal": ContractRenewal,
        "DataPlan": DataPlan,
        "DataUsage": DataUsage,
        "CustServCalls": CustServCalls,
        "DayMins": DayMins,
        "DayCalls": DayCalls,
        "MonthlyCharge": MonthlyCharge,
        "OverageFee": OverageFee,
        "RoamMins": RoamMins
    }

    response = requests.post(" https://customer-churn-prediction-ml-project-3.onrender.com ", json=data)

    prediction = response.json()["prediction"]

    if prediction == 1:
        st.error("Customer will Churn ❌")
    else:
        st.success("Customer will Stay ✅")

