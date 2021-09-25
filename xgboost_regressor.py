# -*- coding: utf-8 -*-
"""xgboost-regressor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eNZhlvi3uouWib-cDuHDJ_FIWfpqh77f
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

combined_data = pd.read_csv('cleaned_data.csv')

combined_data.head()

X = combined_data.iloc[:, :-1].values
y = combined_data.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)

"""## XGBOOST REGRESSOR"""

from xgboost import XGBRegressor
xgb = XGBRegressor()
xgb.fit(X_train, y_train)

f'Coefficient of determination R^2 on train set {xgb.score(X_train, y_train)}'
# must be close to 1, 1 is perfect fit

f'Coefficient of determination R^2 on test set {xgb.score(X_test, y_test)}'

"""### OVERFIT MODEL"""

from sklearn.model_selection import cross_val_score
score = cross_val_score(xgb, X, y, cv = 3)

score.mean()

pred = xgb.predict(X_test)

sns.distplot(y_test - pred)

"""#### HYPERPARAMETER TUNING"""

n_estimators = [int(x) for x in np.linspace(start=100, stop=1200, num=12)]
learning_rate = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
max_depth = [int(x) for x in np.linspace(5, 30, num=6)]
subsample = [0.7, 0.6, 0.8]
min_child_weight = list(range(3, 8))
objective = ['reg:squarederror']
params = {
    'n_estimators': n_estimators,
    'learning_rate': learning_rate,
    'max_depth': max_depth,
    'subsample': subsample,
    'min_child_weight': min_child_weight,
    'objective': objective
}

from sklearn.model_selection import RandomizedSearchCV
search = RandomizedSearchCV(xgb, params, scoring='neg_mean_squared_error', 
                            cv=5, n_iter=100, random_state=43, n_jobs=-1, verbose=True)
search.fit(X,y)

search.best_params_

search.best_score_

pred = search.predict(X_test)
sns.distplot(y_test-pred)

from sklearn import metrics
print(f"Mean Abs Error: {metrics.mean_absolute_error(y_test, pred)}")
print(f"Mean Sq Error: {metrics.mean_squared_error(y_test, pred)}")
print(f"Root Mean Error: {np.sqrt(metrics.mean_squared_error(y_test, pred))}")

search.best_estimator_

import pickle
pickle.dump(search, open('xgb.pkl', 'wb'))

