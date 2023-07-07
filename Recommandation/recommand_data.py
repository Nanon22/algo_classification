from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies

critics = {
    'Lisa Rose': 
    {
        'Lady in the Water': 2.5, 
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0, 
        'Superman Returns': 3.5, 
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': 
    {
        'Lady in the Water': 3.0, 
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5, 
        'Superman Returns': 5.0, 
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5
    },
    'Michael Phillips': 
    {
        'Lady in the Water': 2.5, 
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5, 
        'The Night Listener': 4.0
    },
    'Claudia Puig': 
    {
        'Snakes on a Plane': 3.5, 
        'Just My Luck': 3.0,
        'The Night Listener': 4.5, 
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5
    },
    'Mick LaSalle': 
    {
        'Lady in the Water': 3.0, 
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0, 
        'Superman Returns': 3.0, 
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0
    },
    'Jack Matthews': 
    {
        'Lady in the Water': 3.0, 
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0, 
        'Superman Returns': 5.0, 
        'You, Me and Dupree': 3.5
    },
    'Toby': 
    {
        'Snakes on a Plane':4.5,
        'You, Me and Dupree':1.0,
        'Superman Returns':4.0
    }
}

Movies = {
        'Lady in the Water': 0.0, 
        'Snakes on a Plane': 0.0,
        'Just My Luck': 0.0, 
        'Superman Returns': 0.0, 
        'You, Me and Dupree': 0.0,
        'The Night Listener': 0.0
    }


def eucli(person1 : dict, person2 : dict) :
    common_keys = person1.keys() & person2.keys()

    parts = []

    for key in common_keys :
        parts.append((person1[key] - person2[key])**2)

    dist_eucli = sqrt(sum(parts))

    return 1/(1 + dist_eucli)

def pearson(person1 : dict, person2 : dict) :
    common_keys = person1.keys() & person2.keys()

    n = len(common_keys)

    products = []
    person1_notes = []
    person2_notes = []

    for key in common_keys :
        products.append(person1[key] * person2[key])
        person1_notes.append(person1[key])
        person2_notes.append(person2[key])

    person1_notes_squared = list(map((lambda x: x **2), person1_notes))
    person2_notes_squared = list(map((lambda x: x **2), person2_notes))

    r = (n*sum(products) - (sum(person1_notes)*sum(person2_notes)))/sqrt((n*sum(person1_notes_squared)- sum(person1_notes)**2)*(n*sum(person2_notes_squared)- sum(person2_notes)**2))

    return r

def similarity(critics : dict, person_name : str) :
    if person_name in critics : person = critics.pop(person_name)
    else : return

    different_keys = Movies.keys() - person.keys()

    similarities = {}
    movie_notes = {}

    for key in critics :
        other_person = critics[key]
        similarity = pearson(person, other_person)
        if similarity < 0 : continue
        for movie in different_keys:
            if movie in other_person :
                if not movie in movie_notes: movie_notes[movie] = 0
                if not movie in similarities: similarities[movie] = 0

                movie_notes[movie] += other_person[movie] * similarity
                
                similarities[movie] += similarity

    return dict(map((lambda x: (x[0], x[1]/similarities[x[0]])), sorted(movie_notes.items())))  


