# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:54:19 2021

@author: juanr
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def input(X):
  scaler = MinMaxScaler()
  X_train = scaler.fit_transform(X)
  X_train = pd.DataFrame(X_train, columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal'])
  return(X_train)

def model_predict(X):
  from sklearn.externals import joblib
  loaded_model = joblib.load(r'content/y2_model_joblib')
  result = loaded_model.predict(X)
  print(result)
