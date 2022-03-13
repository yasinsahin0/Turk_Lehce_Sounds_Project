import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Kidem_ve_Maas_VeriSeti.csv')

X = dataset.iloc[:, :-1].values # tek sütun olsada bir matris onu vektöre çevirdik
y = dataset.iloc[:, 1].values # bir vektör olduğu için stünü direk aldık


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

regressor = LinearRegression() # lineer reg sınıfından nesne oluşturuyoruz.

regressor.fit(X_train, y_train) # model eğitimi yapıyoruz
#print(X_test)
a = np.array([[1.0],[2.0]])
print(a)
y_pred = regressor.predict(a)
print(y_pred)
