# Farshad Feyzi 35573143.  ICS 32 Lab sec 8.  Lab asst 3.

import json
import urllib.parse
import urllib.request

def build_search_url(locations: [str]) -> str:
    '''
    This function takes a list of locations and builds and returns a URL that
    can be used to ask the Mapquest Data API for information regarding the
    whole trip
    '''
    # Constants
    MAPQUEST_API_KEY = 'Fmjtd%7Cluu8216tl9%2C2n%3Do5-942s1y'
    BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'
    
    query_parameters = [
        ('from', locations[0])
    ]

    for x in range(len(locations) - 1):
        query_parameters.append(('to', locations[x+1]))

    return BASE_MAPQUEST_URL + '/route?key=' + MAPQUEST_API_KEY + '&' + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> 'json':
    '''
    This function takes a URL and returns a Python object representing the
    parsed JSON response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

def directions(json_result: 'json') -> [str]:
    '''
    Returns a list with the directions from the starting location to the
    final destination
    '''
    directions = []
    
    for item in json_result['route']['legs']:
        for maneuver in item['maneuvers']:
            directions.append(maneuver['narrative'])

    return directions

def total_distance(json_result: 'json') -> int:
    '''
    Returns the total distance of the trip specified
    '''
    return json_result['route']['distance']

def total_time(json_result: 'json') -> int:
    '''
    Returns the total time of the trip specified
    '''
    return json_result['route']['time']

def lat_long(json_result: 'json') -> [dict]:
    '''
    Returns a list with the latitude and longitude of each location
    '''
    lat_longs = []
    
    for item in json_result['route']['locations']:
        lat_longs.append(item['latLng'])

    return lat_longs
