import pandas as pd 

files = ['25-26.csv', '20-21.csv', '21-22.csv', '22-23.csv', '23-24.csv', '24-25.csv']

columns = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG','FTR']

home_form = []
away_form = []

# Combine All The CSV Files
df = pd.concat(
    [pd.read_csv(f, usecols=columns) for f in files],
    ignore_index=True
)

# Sort According To Date
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date").reset_index(drop=True)

# Converting Full Time Results To Numbers From H,A,D
df["Result"] = df["FTR"].replace({
    "H" : 1,
    "A" : 2,
    "D" : 0
})

# Adding Six Additional Columns For Form Tracking
new_cols = ['home_form', 'away_form', 'home_goal_last5', 'away_goal_last5', 'home_win_rate', 'away_win_rate','Home_GD_last5','Away_GD_last5']
for col in new_cols:
    df[col] = 0.0

# Get All Previous Matches For A Team Before A Given Date
def getPreviousMatches(df, teamName, current_date):
    previous = df[
        (
            (df["HomeTeam"] == teamName) | 
            (df["AwayTeam"] == teamName)
        ) &
            (df["Date"] < current_date)
    ]

    return previous.sort_values("Date")

# Calculate Form For A Team Based On Last N Matches, 3 Points For Win, 1 Point For Draw, 0 For Loss
def calculateForm(previous_matches, team, n=5):
    
    last_n = previous_matches.tail(n)
    points = 0 

    for _, x in last_n.iterrows():
        if x["HomeTeam"] == team:
            if x["Result"] == 1:
                points = points + 3
            elif x["Result"] == 0:
                points = points + 1
        elif x["AwayTeam"] == team:
            if x["Result"] == 2:
                points = points + 3
            elif x["Result"] == 0:
                points = points + 1

    return points 

# Calculate Total Goals Scored By A Team In Last N Matches
def calculateGoals(previous_matches, team, n = 5 ):
    last_n = previous_matches.tail(n)
    goals = 0

    for _, x in last_n.iterrows():
        if x["HomeTeam"] == team:
            goals = goals + x["FTHG"]
        if x["AwayTeam"] == team:
            goals = goals + x["FTAG"]

    return goals

# Calculate Win Rate For A Team Based On All Previous Matches
def calculateWinRate(previous_matches, team):

    matches = len(previous_matches)

    if matches == 0:
        return 0
    
    wins = 0

    for _, x in previous_matches.iterrows():
        if x["HomeTeam"] == team and x["Result"] == 1:
            wins = wins + 1
        elif x["AwayTeam"] == team and x["Result"] == 2:
            wins = wins + 1

    return wins/matches

def calculateGoalDifference(previous_matches, team, n=5):
    last_n = previous_matches.tail(n)
    gd = 0

    for _, x in last_n.iterrows():
        if x["HomeTeam"] == team:
            gd = (gd + x["FTHG"]) - x["FTAG"]
        elif x["AwayTeam"] == team:
            gd = gd + x["FTAG"] - x["FTHG"]

    return gd


# Iterate Through Each Match, Get Previous Matches For Both Teams, Calculate Form, Goals Scored And Win Rate, And Update The DataFrame
for i, row in df.iterrows():
    home_team = row["HomeTeam"]
    away_team = row["AwayTeam"]
    match_date = row["Date"]

    home_prev = getPreviousMatches(df, home_team, match_date)
    away_prev = getPreviousMatches(df, away_team, match_date)

    df.at[i, "home_form"] = calculateForm(home_prev, home_team)
    df.at[i, "away_form"] = calculateForm(away_prev, away_team)
    df.at[i, "home_goal_last5"] = calculateGoals(home_prev, home_team)
    df.at[i, "away_goal_last5"] = calculateGoals(away_prev, away_team)
    df.at[i, "home_win_rate"] = calculateWinRate(home_prev, home_team)
    df.at[i, "away_win_rate"] = calculateWinRate(away_prev, away_team)
    df.at[i, "Home_GD_last5"] = calculateGoalDifference(home_prev, home_team)
    df.at[i, "Away_GD_last5"] = calculateGoalDifference(away_prev, away_team)
    

# Save And Create A new CSV File With All The Combined Data And New Features
df.to_csv("combined.csv", index=False)





