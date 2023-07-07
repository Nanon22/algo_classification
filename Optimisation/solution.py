from __future__ import annotations
from functools import reduce
from flight import Flight
from utils import time_to_str

# classe identifiant une solution de notre problème
class Solution:
    def __init__(self, departure_flights : list[Flight], return_flights : list[Flight]):
      self.departure_flights = departure_flights
      self.return_flights = return_flights

    # methode retournant les vols de chaque jour durant le départ 
    def get_departure_days(self) -> list[Flight]:

      flights_by_day = {}

      for flight in self.departure_flights:
        if not str(flight.arrival.day) in flights_by_day: flights_by_day[str(flight.arrival.day)] = []
        flights_by_day[str(flight.arrival.day)].append(flight)
      
      return flights_by_day
    
    # methode retournant les vols de chaque jour durant le retour 
    def get_return_days(self) -> list[Flight]:

      flights_by_day = {}

      for flight in self.return_flights:
        if not str(flight.depart.day) in flights_by_day: flights_by_day[str(flight.depart.day)] = []
        flights_by_day[str(flight.depart.day)].append(flight)
      
      return flights_by_day

    # methode retournant le temps maximal d'attente au départ
    def departure_waiting_time(self):

      flights_by_day = self.get_departure_days()
      
      waiting_time = []
      for day in flights_by_day:

        first_arrived = min(flights_by_day[day], key = lambda k : k.arrival.timestamp())
        last_arrived = max(flights_by_day[day], key = lambda k : k.arrival.timestamp())

        waiting_time.append((last_arrived.arrival - first_arrived.arrival).total_seconds())
      
      return max(waiting_time)
    
    # methode retournant le temps maximal d'attente au retour
    def arrival_waiting_time(self):

      flights_by_day = self.get_return_days()

      waiting_time = []
      for day in flights_by_day:

        first_departure = min(flights_by_day[day], key = lambda k : k.depart.timestamp())
        last_departure = max(flights_by_day[day], key = lambda k : k.depart.timestamp())

        waiting_time.append((last_departure.depart - first_departure.depart).total_seconds())
      
      return max(waiting_time)
      
    # methode retournant le cout du voyage au départ
    def departure_flights_weight(self):
      return reduce(lambda a, b : a + b.get_weight(), self.departure_flights, 0) + self.departure_waiting_time()
    
    # methode retournant le cout du voyage au retour
    def return_flights_weight(self):
      return reduce(lambda a, b : a + b.get_weight(), self.return_flights, 0) + self.arrival_waiting_time()
    
    # methode retournant les frais additionnels associciés à la solution
    def additionnal_fees(self):
      fees = 0
      departure_days : list[Flight] = self.get_departure_days()
      return_days : list[Flight] = self.get_return_days()
      if(len(departure_days) > 1) : fees += 200
      if(len(return_days) > 1) : fees += 200
      
      for day in departure_days:
        if max(departure_days[day], key = lambda k : k.arrival.hour).arrival.hour > 17: fees += 100
      for day in return_days:
        if max(return_days[day], key = lambda k : k.depart.hour).depart.hour < 17: fees += 100

      return fees

    # methode retournant le cout total de la solution
    def global_travel_weight(self):
      return self.departure_flights_weight() + self.return_flights_weight() + self.additionnal_fees()
    
    # methode retournant la somme d'argent déboursé au départ
    def departure_price(self):
      return reduce(lambda a, b : a + b.price, self.departure_flights, 0)
    
    # methode retournant la somme d'argent déboursé au retour
    def return_price(self):
      return reduce(lambda a, b : a + b.price, self.return_flights, 0)
    
    # methode retournant la somme d'argent déboursé pour cette solution
    def global_price(self):
      return self.departure_price() + self.arrival_price() + self.additionnal_fees()
    
    # methode retournant l'ensemble des voisiin de la solution
    def neighbors(self) -> list[Solution]:
      neighbors : list(Solution) = []
      for index, flight in enumerate(self.departure_flights):
        departure_flights_copy = self.departure_flights.copy()
        del departure_flights_copy[index]

        if(flight.left_neighbor != None):
          neighbors.append(Solution(
            departure_flights = departure_flights_copy + [flight.left_neighbor],
            return_flights = self.return_flights.copy()
          ))
        if(flight.right_neighbor != None):
          neighbors.append(Solution(
            departure_flights = departure_flights_copy + [flight.right_neighbor],
            return_flights = self.return_flights.copy()
          ))

      for index, flight in enumerate(self.return_flights):
        return_flights_copy = self.return_flights.copy()
        del return_flights_copy[index]

        if(flight.left_neighbor != None):
          neighbors.append(Solution(
            departure_flights = self.departure_flights.copy(),
            return_flights = return_flights_copy + [flight.left_neighbor]
          ))
        if(flight.right_neighbor != None):
          neighbors.append(Solution(
            departure_flights = self.departure_flights.copy(),
            return_flights = return_flights_copy + [flight.right_neighbor]
          ))
      return neighbors
    
    # methode retournant le meilleur voisin de la solution en précisant s'il est meilleur que la solution ou pas.
    def best_neighbor(self):
      best_neighbor = min(self.neighbors(), key = lambda x : x.global_travel_weight())

      if(best_neighbor.global_travel_weight() < self.global_travel_weight()) : return (True, best_neighbor)
      else : return (False, best_neighbor)
    
    # methode permettant d'obtenir un résumé de la solution
    def to_string(self):
      return "cette solution coûtera {}€ pour l'aller et {}€ pour le retour donc {}€ au total. Le plus long temps d'attente au départ est de {} et le plus long temps d'attente au retour est de {}.".format(self.departure_price(), self.return_price(), self.global_price(), time_to_str(self.departure_waiting_time()), time_to_str(self.arrival_waiting_time()))