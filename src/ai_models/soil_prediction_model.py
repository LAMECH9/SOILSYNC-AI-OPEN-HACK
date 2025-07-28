# src/ai_models/soil_prediction_model.py
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from imblearn.over_sampling import SMOTE
from sklearn.feature_selection import SelectFromModel

class SoilPredictionModel:
    def __init__(self):
        self.features = [
            'soil ph', 'total nitrogen', 'phosphorus olsen', 'potassium meq',
            'calcium meq', 'magnesium meq', 'manganese meq', 'copper', 'iron',
            'zinc', 'sodium meq', 'total org carbon', 'NDVI', 'soil_moisture',
            'real_time_ph', 'salinity_ec', 'crop_stress', 'yellowing_leaves',
            'rainfall_mm', 'temperature_c'
        ]
        self.scaler = StandardScaler()
        self.rf_nitrogen = RandomForestClassifier(random_state=42)
        self.rf_phosphorus = RandomForestClassifier(random_state=42)
        self.selected_features = None

    def preprocess_data(self, data):
        """Preprocess and scale features, handling missing values"""
        X = data[self.features].fillna(data[self.features].mean(numeric_only=True))
        return self.scaler.fit_transform(X)

    def train(self, data, target_nitrogen='total nitrogenclass', target_phosphorus='phosphorus olsen class'):
        """Train models for nitrogen and phosphorus prediction"""
        # Encode targets
        data[target_nitrogen] = data[target_nitrogen].map({'low': 0, 'adequate': 1, 'high': 2})
        data[target_phosphorus] = data[target_phosphorus].map({'low': 0, 'adequate': 1, 'high': 2})
        data = data.dropna(subset=[target_nitrogen, target_phosphorus])

        X = self.preprocess_data(data)
        y_nitrogen = data[target_nitrogen]
        y_phosphorus = data[target_phosphorus]

        # Handle class imbalance with SMOTE
        smote = SMOTE(random_state=42)
        X_balanced, y_nitrogen_balanced = smote.fit_resample(X, y_nitrogen)

        # Split data
        X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(
            X_balanced, y_nitrogen_balanced, test_size=0.2, random_state=42
        )
        X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(
            X, y_phosphorus, test_size=0.2, random_state=42
        )

        # Feature selection for nitrogen
        rf_selector = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_selector.fit(X_train_n, y_train_n)
        selector = SelectFromModel(rf_selector, prefit=True)
        self.selected_features = [self.features[i] for i in selector.get_support(indices=True)]

        # Train nitrogen model with hyperparameter tuning
        param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [10, 20, None],
            'min_samples_split': [2, 5],
            'min_samples_leaf': [1, 2]
        }
        grid_search = GridSearchCV(self.rf_nitrogen, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
        grid_search.fit(selector.transform(X_train_n), y_train_n)
        self.rf_nitrogen = grid_search.best_estimator_

        # Train phosphorus model
        self.rf_phosphorus.fit(X_train_p, y_train_p)

        # Evaluate
        nitrogen_accuracy = self.rf_nitrogen.score(selector.transform(X_test_n), y_test_n)
        phosphorus_accuracy = self.rf_phosphorus.score(X_test_p, y_test_p)
        return {
            'nitrogen_accuracy': nitrogen_accuracy,
            'phosphorus_accuracy': phosphorus_accuracy,
            'avg_accuracy': (nitrogen_accuracy + phosphorus_accuracy) / 2
        }

    def predict(self, data):
        """Predict nitrogen and phosphorus status"""
        X = self.preprocess_data(data)
        nitrogen_pred = self.rf_nitrogen.predict(X[:, [self.features.index(f) for f in self.selected_features]])
        phosphorus_pred = self.rf_phosphorus.predict(X)
        return pd.DataFrame({
            'nitrogen_class': nitrogen_pred,
            'phosphorus_class': phosphorus_pred
        })
