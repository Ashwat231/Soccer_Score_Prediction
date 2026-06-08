import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import (accuracy_score)
from xgboost import XGBClassifier

import joblib

# Loading The Dataset
df = pd.read_csv('combined.csv')

# Required Features/Columns For train/test
features = ["home_form", "away_form", "home_goal_last5", "away_goal_last5", "home_win_rate", "away_win_rate", "Home_GD", "Away_GD"]

# 80% For Training
train = int(len(df) * 0.8)

train_df = df.iloc[:train] # Training Dataset, 80%, Gets all columns and rows before :80%
test_df = df.iloc[train:] # Testing Dataset, 20% , Gets all columns and rows after :20%

X_train = train_df[features] # Get Features Only 
y_train = train_df["Result"] # Get Result Only

X_test = test_df[features] # Get Features Only
y_test = test_df["Result"] # Get Result Only

#---------------------------------------------------------------------------------------
# Logistic Regression Prediction Model

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
# Prediction
prediction = model.predict(X_test)
logistic = accuracy_score(y_test, prediction)

print("Accuracy For Logistic Regression: ", logistic)
joblib.dump(model, 'logistic_model.pkl')

#------------------------------------------------------------------------------------------
# Random Forest Prediction model

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)
#Prediction
prediction = model.predict(X_test)
forest = accuracy_score(y_test, prediction)

print("Accuracy For Random Forest: ", forest)
joblib.dump(model, 'forest_model.pkl')

#------------------------------------------------------------------------------------------
# XGBoost

model = XGBClassifier(n_estimators = 200, learning_rate = 0.1, max_depth = 4, random_state = 42, eval_metric = 'logloss')
model.fit(X_train, y_train)
#Prediction
prediction = model.predict(X_test)
xg = accuracy_score(y_test, prediction)

print("Accuracy For XGBoost: ", xg)
joblib.dump(model, 'xgboost_model.pkl')