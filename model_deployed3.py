# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:58:33 2021

@author: juanr
"""



import streamlit as st

import model_functions as m

import pandas as pd

import numpy as np

st.title("Heart Disease predictor")
st.header("Introduce the following features and our product will predict acute heart disease")

t1 = st.number_input("input age")
t2 = st.number_input(" input sex")
t3 = st.number_input(" input chest pain type ")
t4 = st.number_input(" input resting blood pressure")
t5 = st.number_input(" input serum cholesterol in mg/dl")
t6 = st.number_input(" input fasting blood sugar")
t7 = st.number_input(" input resting electrocardiographic results(values 0,1,2")
t8 = st.number_input(" inout max heart reat achieved")
t9= st.number_input(" input exercised induced angina")
t10 = st.number_input(" input oldpeak = ST depression induced by exercise relative ro rest")
t11 = st.number_input(" the slope of the peak exercise ST segment")
t12 = st.number_input(" number of najor vessels (0-3) coloured by flourosopy")
t13 = st.number_input(" thal")


if t13 != 0:
    X = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13]
    df = pd.DataFrame(X)
    input_data = m.input(df.T)
    model_predictor = m.model_predict(input_data)
    print(model_predictor)


