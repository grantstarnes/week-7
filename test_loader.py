import unittest
import pandas as pd
from loader import get_geolocator, fetch_location_data, build_geo_dataframe

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        
        geolocator = get_geolocator("test_valid_locations")

        locations = [
            "Museum of Modern Art",
            "USS. Alabama Battleship Memorial Park"
        ]
        
        location_data = {
            "Museum of Modern Art": {
                "latitude": 40.7618552,
                "longitude": -73.9782438,
                "type": "Museum"
            },
            "USS Alabama Battleship Memorial Park": {
                "latitude": 30.684373,
                "longitude": -88.015316,
                "type": "Park"
            }
        }

        df = build_geo_dataframe(geolocator, locations)

        self.assertEqual(len(df), 2)

        for _, row in df.iterrows():
            loc = row["location"]
            self.assertIn(loc, location_data)
            self.assertAlmostEqual(row["latitude"], location_data[loc]["latitude"], delta = 0.01)
            self.assertAlmostEqual(row["longitude"], location_data[loc]["longitude"], delta = 0.01)
            self.assertEqual(row["type"].lower(), location_data[loc]["type"].lower())

    def test_invalid_location(self):
        geolocator = get_geolocator("test_invalid_location")
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertIsInstance(result, dict, "Result should be a dictionary")

        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertIsNone(result["latitude"], "Latitude should be None for invalid location")
        self.assertIsNone(result["longitude"], "Longitude should be None for invalid location")
        self.assertIsNone(result["type"], "Type should be None for invalid location")

if __name__ == "__main__":
    unittest.main()
