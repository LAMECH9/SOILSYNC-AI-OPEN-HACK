# src/database/data_fusion.py
import pandas as pd
import numpy as np
from data_processing.soilhive_data_integration import SoilHiveDataIntegration
from data_processing.satellite_data_processor import SatelliteDataProcessor
from data_processing.iot_sensor_interface import IoTSensorInterface

class DataFusion:
    def __init__(self, soilhive_api_key, satellite_api_key):
        self.soilhive = SoilHiveDataIntegration(soilhive_api_key)
        self.satellite = SatelliteDataProcessor(satellite_api_key, num_samples=0)
        self.num_samples = 0

    def fuse_data(self, region, date_range, soil_data):
        """Integrate data from multiple sources"""
        self.num_samples = len(soil_data)
        self.satellite.num_samples = self.num_samples
        self.iot = IoTSensorInterface(soil_data)

        satellite_data = self.satellite.fetch_imagery(region, date_range)
        iot_data = self.iot.get_latest_data()
        farmer_data = pd.DataFrame({
            'crop_stress': np.random.choice([0, 1], size=self.num_samples, p=[0.7, 0.3]),
            'yellowing_leaves': np.where(
                soil_data['total nitrogen'] < 0.2,
                np.random.choice([0, 1], size=self.num_samples, p=[0.4, 0.6]),
                np.random.choice([0, 1], size=self.num_samples, p=[0.9, 0.1])
            )
        })
        climate_data = pd.DataFrame({
            'rainfall_mm': np.random.normal(600, 100, self.num_samples),
            'temperature_c': np.random.normal(25, 2, self.num_samples)
        })

        return pd.concat([
            soil_data.reset_index(drop=True),
            satellite_data.reset_index(drop=True),
            iot_data.reset_index(drop=True),
            farmer_data.reset_index(drop=True),
            climate_data.reset_index(drop=True)
        ], axis=1)
