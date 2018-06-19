# Farshad Feyzi 35573143.  ICS 32 Lab sec 8.  Lab asst 3.

import mapquest_interaction

class Steps:
    '''
    Class that prints the directions
    '''
    def generate(self, json_result) -> None:
        '''
        Prints the directions
        '''
        directions = mapquest_interaction.directions(json_result)
        print('DIRECTIONS')
        for direction in directions:
            print(direction)
        print()

class TotalDistance:
    '''
    Class that prints the total distance
    '''
    def generate(self, json_result) -> None:
        '''
        Prints the total distance
        '''
        distance = round(abs(mapquest_interaction.total_distance(json_result)))
        print('Total Distance: ' + str(abs(distance)) + ' miles')
        print()

class TotalTime:
    '''
    Class that prints the total time
    '''
    def generate(self, json_result) -> None:
        '''
        Prints the total time
        '''
        minutes = round(abs(mapquest_interaction.total_time(json_result)/60))
        print('Total Time: ' + str(abs(minutes)) + ' minutes')
        print()

class LatLong:
    '''
    Class that prints the latitude and longitude of each location
    '''
    def generate(self, json_result) -> None:
        '''
        Prints the latitude and longitude of each location
        '''
        lat_longs = mapquest_interaction.lat_long(json_result)
        latitude = ''
        longitude = ''
        for dictionary in lat_longs:
            if dictionary['lat'] >= 0:
                latitude = str(round(dictionary['lat'], 2)) + 'N '
            elif dictionary['lat'] < 0:
                latitude = str(round(abs(dictionary['lat']), 2)) + 'S '
            if dictionary['lng'] >= 0:
                longitude = str(round(dictionary['lng'], 2)) + 'E'
            elif dictionary['lng'] < 0:
                longitude = str(round(abs(dictionary['lng']), 2)) + 'W'

            print(latitude + longitude)
        print()

