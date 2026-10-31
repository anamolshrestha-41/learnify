import joblib
import pandas as pd
from pathlib import Path

model=joblib.load("../models/best_futsal_model.pkl")
def predict_goal(shot_distance, shot_angle, defensive_pressure, goalkeeper_distance):
    input_data=pd.DataFrame([{
        "shot_distance": shot_distance,
        "shot_angle":shot_angle,
        "defensive_pressure":defensive_pressure,
        "goalkeeper_distance":goalkeeper_distance
    }])
    probability=model.predict_proba(input_data)[0][1]
    prediction=int(probability>=0.5)
    result="GOAL" if prediction==1 else "NO GOAL"
    return{
        "prediction":result,
        "goal_probability":round(float(probability), 4)
    }

if __name__ == "__main__":
    result=predict_goal(
        shot_distance=3,
        shot_angle=10,
        defensive_pressure=1,
        goalkeeper_distance=10
    )
    print(result)