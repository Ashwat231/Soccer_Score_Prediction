import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score)

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

# Logistic Regression Prediction Model
model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

# Prediction
prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))