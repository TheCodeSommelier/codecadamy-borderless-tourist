destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]


# This function gets the index of the destination in the "destinations" list
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


# This function gets travelers location
def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# This loop creates empty lists for future attractions. Number of lists is based on destinations
attractions = [[] for element in destinations]

# This function lets you add attractions to the attratctions sublists
def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destinations = attractions[destination_index]
    attractions_for_destinations.append(attraction)
    return attractions_for_destinations

# Here I added some attractions
add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])

# This function finds attractions based on interests of the traveler 
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interests = []
    
    for attraction in attractions_in_city:
        possible_attraction = attraction
        for interest in interests:
            if interest in possible_attraction[1]:
                attractions_with_interests.append(possible_attraction[0])
    return attractions_with_interests

la_arts = find_attractions("Los Angeles, USA", ["art"])

# This function returns a string greeting the traveler and suggesting attractions based on their interests
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination
    for attraction in traveler_attractions:
        interests_string = interests_string + ", " + attraction
    return interests_string

# Here I defined one traveler. Feel free to change the lists or add new function calls
smills_france = get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]])

# Remeber to print the results of calling get_attractions_for_traveler with your traveler to see the result! 😁
print(smills_france)