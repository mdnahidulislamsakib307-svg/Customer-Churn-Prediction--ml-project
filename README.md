# Customer-Churn-Prediction--ml-project
# Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Render](https://img.shields.io/badge/Deployment-Render-purple)

## Project Overview

This project predicts **customer churn** for a telecom company using a machine learning model.  
It includes:

- **ML Model**: Logistic Regression trained on telecom customer dataset
- **API**: FastAPI backend serving predictions
- **Web App**: Streamlit frontend for interactive user input
- **Deployment**: Hosted on Render

Users can input customer details, and the system predicts if the customer is likely to **churn** or **stay**.

---

## Dataset

- Dataset: `telecom_churn.csv`  
- Target Column: `Churn` (1 = churn, 0 = stay)  
- Features include:
  - `AccountWeeks`, `ContractRenewal`, `DataPlan`, `DataUsage`, `CustServCalls`
  - `DayMins`, `DayCalls`, `MonthlyCharge`, `OverageFee`, `RoamMins`

---

## ML Model

- Model: **Logistic Regression**
- Library: **scikit-learn**
- Model saved as: `LogisticRegression.pkl`

---

## API (FastAPI)

- File: `main.py`
- Endpoint: `/predict`  
- Input: JSON with all customer features (except target)  
- Output: JSON with predicted churn (0 = stay, 1 = churn)  

