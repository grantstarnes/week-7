import unittest
import pandas as pd
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        
        geolocator = get_geolocator()

        location_test = [
            {
                "location": "Museum of Modern Art",
                "latitude": 40.7618552,
                "longitude": -73.9782438,
                "type": "Museum"
            },
            {
                "location": "USS. Alabama Battleship Memorial Park",
                "latitude": 30.684373,
                "longitude": -88.015316,
                "type": "Park"
            }
        ]

        for loc_data in location_test:
            result = fetch_location_data(geolocator, loc_data["location"])

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertTrue(pd.isna(result["latitude"]))
        self.assertTrue(pd.isna(result["longitude"]))
        self.assertTrue(pd.isna(result["type"]))

if __name__ == "__main__":
    unittest.main()
