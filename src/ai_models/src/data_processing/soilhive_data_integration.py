# src/data_processing/soilhive_data_integration.py
import pandas as pd
from api.soilhive_api_client import SoilHiveAPIClient

class SoilHiveDataIntegration:
    def __init__(self, api_key):
        self.api_client = SoilHiveAPIClient(api_key)
        self.required_columns = [
            'soil ph', 'total nitrogen', 'phosphorus olsen', 'potassium meq',
            'calcium meq', 'magnesium meq', 'manganese meq', 'copper', 'iron',
            'zinc', 'sodium meq', 'total org carbon', 'total nitrogenclass',
            'phosphorus olsen class', 'county', 'fertilizer recommendation'
        ]

    def fetch_soil_data(self, region=None):
        """Fetch soil data from SoilHive API"""
        raw_data = self.api_client.get_soil_data(region=region)
        df = pd.DataFrame(raw_data)
        if not all(col in df.columns for col in self.required_columns):
            raise ValueError("Missing required soil data columns")
        return df[self.required_columns]

    def preprocess_data(self, df):
        """Clean and preprocess SoilHive data"""
        return df.fillna(df.mean(numeric_only=True))
