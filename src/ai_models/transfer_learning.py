# src/ai_models/transfer_learning.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE

class TransferLearning:
    def __init__(self):
        self.features = [
            'soil ph', 'total nitrogen', 'phosphorus olsen', 'potassium meq',
            'calcium meq', 'magnesium meq', 'manganese meq', 'copper', 'iron',
            'zinc', 'sodium meq', 'total org carbon', 'NDVI', 'soil_moisture',
            'real_time_ph', 'salinity_ec', 'crop_stress', 'yellowing_leaves',
            'rainfall_mm', 'temperature_c'
        ]
        self.rf_model = RandomForestClassifier(random_state=42)

    def adapt_model(self, new_data, target='total nitrogenclass'):
        """Fine-tune model for data-scarce regions"""
        new_data[target] = new_data[target].map({'low': 0, 'adequate': 1, 'high': 2})
        new_data = new_data.dropna(subset=[target])
        X = new_data[self.features].fillna(new_data[self.features].mean(numeric_only=True))
        y = new_data[target]

        smote = SMOTE(random_state=42)
        X_balanced, y_balanced = smote.fit_resample(X, y)
        self.rf_model.fit(X_balanced, y_balanced)

    def predict(self, data):
        """Predict nutrient status for new regions"""
        X = data[self.features].fillna(data[self.features].mean(numeric_only=True))
        return self.rf_model.predict(X)
