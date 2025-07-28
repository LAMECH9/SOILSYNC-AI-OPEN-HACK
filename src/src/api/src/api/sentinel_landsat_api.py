# src/api/sentinel_landsat_api.py
class SatelliteAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_imagery(self, coordinates, date_range):
        """Placeholder for Sentinel-2/Landsat API"""
        return {}  # Handled by satellite_data_processor.py
