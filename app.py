from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI() # Create Object Instance

class MatchFeatures(BaseModel):
    home_form: float
    away_form: float
    home_goal_last5: float
    away_goal_last5: float
    home_win_rate: float
    away_win_rate: float
    Home_GD: float
    Away_GD: float

# Load The Saved Models
forest = joblib.load("forest_model.pkl")
logistic = joblib.load("logistic_model.pkl")
xgboost = joblib.load("xgboost_model.pkl")

@app.get("/") # When root(/) is called, return the following is executed. This is called the Decorator.
def root(): # Function called when root(/) request is made
    return {
        "message" : "Soccer Match Prediction API"
    }


@app.post("/predict")
def predict(match:MatchFeatures):
    features = [[
        match.home_form,
        match.away_form,
        match.home_goal_last5,
        match.away_goal_last5,
        match.home_win_rate,
        match.away_win_rate,
        match.Home_GD,
        match.Away_GD
    ]]

    predict1 = logistic.predict(features)[0]
    predict2 = forest.predict(features)[0]
    predict3 = xgboost.predict(features)[0]

    labels = {
        0 : "Draw",
        1 : "Home Win",
        2 : "Away Win"
    }

    return {
        "predict1" : labels[int(predict1)],
        "predict2" : labels[int(predict2)],
        "predict3" : labels[int(predict3)],
    }
