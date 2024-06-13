from opencage.geocoder import OpenCageGeocode
import requests
import setup as s

api_key = s.getOpenCageToken()


def get_coordinates(place_description) -> tuple:
    geocoder = OpenCageGeocode(api_key)
    result = geocoder.geocode(place_description, bounds_us = "24.396308,-125.000000,49.384358,-66.934570")

    if result and len(result):
        location = result[0]['geometry']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None
    
def get_address_from_latlng(latitude, longitude) -> int:
    base_url = "https://api.opencagedata.com/geocode/v1/json"

    params = {
        "q": f"{latitude},{longitude}",
        "key": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["results"]: return data["results"][0]["formatted"]

    return response.status_code

def check_location(place_description: str=None) -> tuple:
    if place_description is None:
        print("No Location Given")
        return None
    coordinates = get_coordinates(place_description)

    if coordinates:
        latitude, longitude = coordinates
        #print(f"Latitude: {latitude}, Longitude: {longitude}")
        #print(get_address_from_latlng(latitude, longitude))
        return latitude, longitude
    else:
        print("Location not found.")
        return None

#check_location()