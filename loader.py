'''
Script to load geographical data into a pandas DataFrame, and save it as a CSV file.
'''

import numpy as np
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
    '''
    This function retrieves various aspects of geographic information, such as
    latitude, longitude, amd type for the provided location name, as long as it is
    a valid location. It takes in geolocator and loc as parameters, and returns 
    a dictionary with location, latitude, longitude, and type, and if the location
    isn't valid, it fills the remaining latitude, longitude, and type as NaN.
    '''
    try:
        location = geolocator.geocode(loc)

        if location is None:
            
            return {
                "location": loc,
                "latitude": "nan",
                "longitude": "nan",
                "type": "nan"
            }
        
        return {
            "location": loc,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "type": str(location.raw.get("type", "nan"))
        }
    
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error for location '{loc}': {e}")
        return {
            "location": loc,
            "latitude": "nan",
            "longitude": "nan",
            "type": "nan"
        }

def build_geo_dataframe(geolocator, locations):
    '''
    This function puts together/returns a pandas dataframe that contains the location,
    latitude, longitude, and type for each location using a for loop. 
    '''
    geo_data = [fetch_location_data(geolocator, loc) for loc in locations]

    return pd.DataFrame(geo_data)

if __name__ == "__main__":
    geolocator = get_geolocator()

    locations = ["Museum of Modern Art", "iuyt8765(*&)", "Alaska", "Franklin's Barbecue", "Burj Khalifa"]

    df = build_geo_dataframe(geolocator, locations)

    df.to_csv("./geo_data.csv")
