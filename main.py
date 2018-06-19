# Farshad Feyzi 35573143.  ICS 32 Lab sec 8.  Lab asst 3.

import mapquest_classes
import mapquest_interaction

def location_input() -> [str]:
    '''
    Returns a list of the locations inputted by the user
    '''
    number_of_locations = int(input())
    locations = []

    for location in range(number_of_locations):
        location = input()
        locations.append(location)

    return locations

def outputs() -> list:
    '''
    Returns a list of the classes associated to the output types inputted by
    the user
    '''
    number_of_outputs = int(input())
    outputs = []
    classes = []

    for output in range(number_of_outputs):
        output = input()
        outputs.append(output)

    for output in outputs:
        if output == 'STEPS':
            classes.append(mapquest_classes.Steps())
        elif output == 'TOTALDISTANCE':
            classes.append(mapquest_classes.TotalDistance())
        elif output == 'TOTALTIME':
            classes.append(mapquest_classes.TotalTime())
        elif output == 'LATLONG':
            classes.append(mapquest_classes.LatLong())

    return classes

if __name__ == '__main__':
    
    locations = location_input()
    classes = outputs()
    result = mapquest_interaction.get_result(mapquest_interaction.build_search_url(locations))
    print()

    for x in classes:
        x.generate(result)
        
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
        
