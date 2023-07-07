import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from flight import Flight
import random

# regroupement d'ensemble de méthodes utiles pour la logique de résolution du problème

# permet de changer un entier en string d'au moins 2 caractères
def to_two_digit_str(val : int):
    if len(str(val)) == 1:
        return "0" +  str(val)
    
    return str(val)

# permet de traduire les secondes durée facilement lisible
def time_to_str(sec):
    time_to_str = str(timedelta(seconds=sec))
    sections = time_to_str.split(':')
    return "{}Hour(s), {}Minute(s), {}Second(s)".format(sections[0], sections[1], sections[2])

# parcours les différents fichiers et recense les vols qui nous interressent en fonction des précisions fournies
def get_flights(desired_flights):

    possible_flights = {}

    for desired_flight in desired_flights:

        flights = None
        airports = desired_flight.split('_')

        possible_flights[airports[0] + "_" + airports[1]] : list[Flight] = []
        
        for possible_time in desired_flights[desired_flight]:
            try:
                flights = ET.parse("ThirdParty/FlightData/" + to_two_digit_str(possible_time["max_departure_time"].year) + "/" + to_two_digit_str(possible_time["max_departure_time"].month) + "-" + to_two_digit_str(possible_time["max_departure_time"].day) + "/" + airports[0] + "-" + airports[1] + ".txt").getroot()
            except FileNotFoundError:
                print('no flights for this journey')
                return []
    
            left_neighbor = None
            
            flights[:] = sorted(flights.findall("flight"), key=lambda element: datetime.fromisoformat(element.find("depart").text).timestamp())
            
            for flight in flights:
                possible_depart_time = datetime.fromisoformat(flight.find("depart").text)
                possible_arrival_time = datetime.fromisoformat(flight.find("arrive").text)

                current_flight = Flight(
                    price = int(flight.find("price").text),
                    orig = flight.find("orig").text,
                    dest = flight.find("dest").text,
                    depart = possible_depart_time,
                    arrival = possible_arrival_time,
                    airline_display = flight.find("airline_display").text
                )
                
                current_flight.left_neighbor = left_neighbor

                if left_neighbor != None : left_neighbor.right_neighbor = current_flight

                if(possible_arrival_time < possible_time["max_arrival_time"] and possible_depart_time > possible_time["max_departure_time"]) :
                    possible_flights[airports[0] + "_" + airports[1]].append(current_flight)
                    
                left_neighbor = current_flight
            
    return possible_flights

# permet de génerer aléatoirement une solution allée ou retour
def get_flights_combination(flights):
    flights_combination : list[Flight] = []
    
    for flight in flights:
        flights_combination.append(random.choice(flights[flight]))

    return flights_combination
