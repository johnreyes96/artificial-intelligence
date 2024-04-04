# -*- coding: utf-8 -*-
"""PredictWithCSV.ipynb

Automatically generated by Colaboratory.

data from: https://www.kaggle.com/datasets/vikramtiwari/california-housing-dataset-ml-crash-course
"""

import pandas as pd
import numpy as np
import pickle as pk
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

datos = pd.read_csv('../data/california_housing_train.csv')
copy_datos = datos.copy()
print(datos)

scaler = StandardScaler()
print(np.mean(datos.loc[:, 'total_rooms']))
scaler.fit(datos)
datos = scaler.transform(datos)

# np.mean(scaler.transform(datos)[:,4])
print(np.mean(copy_datos.loc[:, 'total_rooms']))

model = SVR(C=1.0, epsilon=0.2)
model.fit(X=datos[:, 0:4], y=datos[:, -1])

pickle_file = open('../output/modelo', 'wb')
pk.dump(model, pickle_file)

# modelo.predict()  Para predecir
pickle_file = open('../output/modelo', 'rb')
modelo = pk.load(pickle_file)
