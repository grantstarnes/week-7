'''
Script to load geographical data into a pandas DataFrame, and save it as a CSV file.
'''

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import pandas as pd


def get_geolocator(agent='h501-student'):
    """
    Initiate a Nominatim geolocator instance given an `agent`.

    Parameters
    ----------
    agent : str, optional
        Agent name for Nominatim, by default 'h501-student'
    """
    return Nominatim(user_agent=agent)

def fetch_location_data(geolocator, loc):
    try:
        location = geolocator.geocode(loc)

        if location is None:
            print(f"Location not found: '{loc}'")
            return None
        return {
            "location": loc,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "type": location.geo_type
        }
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error for location '{loc}': {e}")
        return None

def build_geo_dataframe(geolocator, locations):
    geo_data = [fetch_location_data(geolocator, loc) for loc in locations]
    
    return pd.DataFrame(geo_data)


if __name__ == "__main__":
    geolocator = get_geolocator()

    locations = ["Museum of Modern Art", "iuyt8765(*&)", "Alaska", "Franklin's Barbecue", "Burj Khalifa"]

    df = build_geo_dataframe(geolocator, locations)

    df.to_csv("./geo_data.csv")
