# ===========================================
# Prediction File
# ===========================================

import joblib
import numpy as np

# Load Saved Model
model = joblib.load("models/liver_model.pkl")

# Load Scaler
scaler = joblib.load("models/scaler.pkl")


def predict_liver_disease(
    age,
    gender,
    total_bilirubin,
    direct_bilirubin,
    alkaline_phosphotase,
    alt,
    ast,
    total_proteins,
    albumin,
    ag_ratio
):
    
    # Convert Gender
    if gender == "Male":
        gender = 1
    else:
        gender = 0

    # Create Input Array
    data = np.array([[
        age,
        gender,
        total_bilirubin,
        direct_bilirubin,
        alkaline_phosphotase,
        alt,
        ast,
        total_proteins,
        albumin,
        ag_ratio
    ]])

    # Scale Input
    data = scaler.transform(data)

    # Predict
    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]
    print("Prediction:", prediction)
    print("Probabilities:", probability)

    confidence = max(probability) * 100
    return prediction, confidence