from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # For connection between localhost and deployed api on render
import joblib
from pydantic import BaseModel # Pydantic validates and converts input data based on python type annotations.
    
app = FastAPI() # Create Object Instance

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

class MatchFeatures(BaseModel): # Creating class for data validation and parsing using python Type annotation
    home_form: float # Python Type Annotation
    away_form: float
    home_goal_last5: float
    away_goal_last5: float
    home_win_rate: float
    away_win_rate: float
    Home_GD: float
    Away_GD: float

# Load The Saved Models
logistic = joblib.load("logistic_model.pkl")
forest = joblib.load("forest_model.pkl")
xgboost = joblib.load("xgboost_model.pkl")

# GET requet created
@app.get("/") # When root(/) is called, return the following is executed. This is called the Decorator.
def root(): # Function called when root(/) request is made
    return {
        "message" : "Soccer Match Prediction API"
    }


#Post request created
@app.post("/predict") # Whenever somebody send a POST request to /predict, run the function below.
def predict(match:MatchFeatures): # match is an object of MatchFeatures which is a JSON file
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

    # Converting numeric result to strings for simplicity 
    labels = { 
        0 : "Draw",
        1 : "Home Win",
        2 : "Away Win"
    }
    
    # Return the following result when post request is called
    return {
        "Logistic Regression prediction" : labels[int(predict1)],
        "Random Forest prediction" : labels[int(predict2)],
        "XGBoost prediction" : labels[int(predict3)],
    }
