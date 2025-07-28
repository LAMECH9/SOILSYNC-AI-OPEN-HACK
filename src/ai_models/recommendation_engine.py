# src/ai_models/recommendation_engine.py
import pandas as pd

class RecommendationEngine:
    def __init__(self):
        self.class_map = {0: 'low', 1: 'adequate', 2: 'high'}

    def generate_recommendations(self, data, crop_type):
        """Generate fertilizer and management recommendations"""
        recommendations = []
        nitrogen_class = self.class_map.get(data['nitrogen_class'].iloc[0], 'adequate')
        phosphorus_class = self.class_map.get(data['phosphorus_class'].iloc[0], 'adequate')
        soil_ph = data['soil ph'].iloc[0]
        org_carbon = data['total org carbon'].iloc[0]

        if nitrogen_class == 'low':
            recommendations.append("Apply 100 kg/acre of N:P:K 23:23:0 at planting. Top dress with 50 kg/acre CAN.")
        if phosphorus_class == 'low':
            recommendations.append("Apply 75 kg/acre of triple superphosphate (TSP) at planting.")
        if soil_ph < 5.5:
            recommendations.append("Apply 300-800 kg/acre of agricultural lime to correct acidity.")
        if org_carbon < 2.0:
            recommendations.append("Apply 2-4 tons/acre of well-decomposed manure or compost.")
        
        return "; ".join(recommendations) if recommendations else "No specific recommendations."
