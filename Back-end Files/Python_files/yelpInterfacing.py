import setup as s
import requests # Requests for APIs
import classes as rclasses
from urllib.parse import urlencode # URL Encoding
import re
from bs4 import BeautifulSoup

# Status Codes:
    # 200 Success
    # 400 Invalid Request
    # 401 Unauthorized
    # 403 Authorization Error
    # 404 Resource Not Found
    # 413 Payload Too Large
    # 429 Rate Limited
    # 500 Internal Server Error
    # 503 Service Unavailable

ENDPOINT_START = "https://api.yelp.com/v3"
YELP_API_KEY = s.getYelpToken()

def searchYelp(location: str = None, longitude: str = None, latitude: str = None, categories: list = None, offset: int = 0, limit: int = 10, price: list = None, openat: int = None, opennow: int = None, reservationdate: str = None, reservationtime: str = None) -> requests.Response:
    # Searches Yelp based on query parameters
    # Parameters:
        # location: str - Location to search for restaurants in
        # longitude: str - Longitude to search for restaurants in
        # latitude: str - Latitude to search for restaurants in
        # categories: list[str] - List of categories to search for
        # limit: int - Number of results to return (default 10, max 20)
        # offset: int - Number of results to skip (default 0)
        # price: list[str] - List of price ranges to filter by (1=$, 2=$$, 3=$$$, 4=$$$$)
        # openat: int - Unix timestamp in seconds for when to search for restaurants
        # opennow: int - Boolean for whether to search for restaurants open now
        # reservationdate: str - Date for when to search for restaurants
        # reservationtime: str - Time for when to search for restaurants
    # Returns:
        # int - API call code or -1 if not enough parameters given
    sort_by = "best_match"
    term = "restaurants"

    
    if location == None:
        location = "Downtown Brooklyn" # Default location is New York City
    
    if categories == []:
        print("No categories given") # If no categories are given it will fail and return None
        return None

    url = ENDPOINT_START + "/businesses/search"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + YELP_API_KEY
    }
    
    params = {
        "sort_by": sort_by, # Sort by best match
        "term": term # Search for restaurants
    }

    if location is not None: params["location"] = location
    if location is not None: params["longitude"] = longitude
    if location is not None: params["latitude"] = latitude
    if categories is not None: params["categories"] = categories
    if limit is not None: params["limit"] = limit
    if offset is not None: params["offset"] = offset
    if openat is not None: params["openat"] = openat
    if opennow is not None: params["opennow"] = opennow
    if price is not None: params["price"] = price
    if reservationdate is not None: params["reservationdate"] = reservationdate
    if reservationtime is not None: params["reservationtime"] = reservationtime
    
    pattern = r'(%(?!2C)\w{2})'

    url += f'?' + urlencode(params)
    url = re.sub(pattern, '', url)
    url = url.replace('+', '%20')

    return requests.get(url, headers=headers)

def getRestaurantReviews(restaurant_id: str = None) -> requests.Response:
    # Searches Yelp for 3 reviews of a restaurant and then will return API call code as return value
    # 200 indicates successful API Call
    if restaurant_id == None:
        return None # -1 Indicates that no input for restraunt reviews was given
    
    url = "https://api.yelp.com/v3/businesses/" + restaurant_id + "/reviews?count=3"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + YELP_API_KEY
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    return response

def parse_information(query: requests.Response) -> rclasses.RestaurantCatalog:
    restaurants = rclasses.RestaurantCatalog()
    for restaurant in query.json()["businesses"]:
        rest = rclasses.Restaurant(restaurant["id"], restaurant["alias"], restaurant["url"], restaurant["name"], 
                                            restaurant["location"]["address1"], restaurant["location"]["city"], 
                                            [r['title'] for r in restaurant["categories"]], 
                                            restaurant["rating"], restaurant["phone"], restaurant["location"]["zip_code"], restaurant["image_url"])
        restaurants.addRestaurant(rest)
    return restaurants

def getWebsiteUrl(business_url: str = None) -> str:
    response = requests.get(business_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        parent_div = soup.find('div', class_='css-u9z0t') # There are multiple that use this class so need to go to the right one

        if parent_div:
            website_text = parent_div.find('a', {'class': 'css-1idmmu3'}).get_text()
            if website_text.count('.') > 0:
                return website_text
    return None


"""
def getRestaurantHighlights(restaurant_id: str) -> int:
    # Searches Yelp for highlights of a restaurant and then will return API call code as return value
    # 200 indicates successful API Call
    url = "https://api.yelp.com/v3/businesses/" + restaurant_id  + "/review_highlights?count=3"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + YELP_API_KEY
    }
    response = requests.get(url, headers=headers)
    print(response.text)

    return response.status_code
"""