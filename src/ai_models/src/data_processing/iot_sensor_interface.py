# src/data_processing/iot_sensor_interface.py
import pandas as pd
import numpy as np

class IoTSensorInterface:
    def __init__(self, soil_data):
        self.soil_data = soil_data

    def get_latest_data(self):
        """Simulate IoT sensor data based on soil data"""
        num_samples = len(self.soil_data)
        return pd.DataFrame({
            'real_time_ph': self.soil_data['soil ph'] + np.random.normal(0, 0.1, num_samples),
            'salinity_ec': self.soil_data['sodium meq'] * 0.1 + np.random.normal(0, 0.05, num_samples)
        })
