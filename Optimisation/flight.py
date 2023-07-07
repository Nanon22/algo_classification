from datetime import datetime

# classe identifiant un vol
class Flight:
    def __init__(self, price : int, orig : str, dest : str, depart : datetime, arrival : datetime, airline_display : str):
      self.price = price
      self.orig = orig
      self.dest = dest
      self.depart = depart
      self.arrival = arrival
      self.airline_display = airline_display
      self.left_neighbor = None
      self.right_neighbor = None

    # methode retournant la durée du vol
    def get_duration(self):
      return (self.arrival - self.depart).total_seconds()
    
    # methode retournant le cout du vol (argent + temps)
    def get_weight(self):
      return self.get_duration() + self.price