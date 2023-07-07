
from data import flights, flights_return
from utils import get_flights_combination, get_flights
from solution import Solution

# déroulement de la logique de résolution du problème
# Cette fonction retourne une solution jugée comme étant raisonnable
# itération represente le nombre de solution à générer aléatoirement pour notre selection de la meilleure
# une fois une solution choisi parmi les solutions aléatoires on parcourt ses voisins dans l'espoir d'obtenir une meilleur solution
# Si un voisin s'avère meilleur il devient alors notre solution et l'on recommence jusqu'à ne plus trouver de meilleur voisiin
def find_solution(iteration) -> Solution:


    possible_solutions : list[Solution] = []

    departure_flights = get_flights(flights)
    return_flights = get_flights(flights_return)

    for i in range(iteration):

        possible_solutions.append(Solution(
            departure_flights = get_flights_combination(departure_flights),
            return_flights = get_flights_combination(return_flights),
        ))

    solution = min(possible_solutions, key = lambda x : x.global_travel_weight())

    has_better_neighbor, best_neighbor = solution.best_neighbor()

    while(has_better_neighbor) :
        solution = best_neighbor
        has_better_neighbor, best_neighbor = solution.best_neighbor()
    
    return solution


solution = find_solution(20000)

print(solution.to_string())