# -*- coding: utf-8 -*-
"""bank_marketing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ae4yjRS63UxULwOB8VwkvZWSWdM6piKm
"""

from google.colab import files
a= files.upload()

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv("bank_marketing.csv")
data.head()

columns = []
for i in data.columns:
  columns.append(i)
columns

for i in columns:
  print("number of unique values is",len(np.unique(data[i])))

data.shape

numerical_column = ['Unnamed: 0','age','balance','day','duration','campaign','pdays','previous']
categorical_column = []
for i in columns:
  if i not in numerical_column:
    categorical_column.append(i)
categorical_column

le = LabelEncoder()
for i in categorical_column:
  data[i] = le.fit_transform(data[i])

sns.countplot(data['deposit'])

x = data.iloc[:,:17].values
y = data.iloc[:,17].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

cls = RandomForestClassifier()
cls.fit(x_train,y_train)

y_pred = cls.predict(x_test)

import matplotlib.pyplot as plt

sns.countplot(data['deposit'],hue=data['job'])

metrics.f1_score(y_test,y_pred)





