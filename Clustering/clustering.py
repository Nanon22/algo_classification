import re
import os
from math import sqrt


def pearson(element1 : dict, element2 : dict) :
    common_keys = element1.keys() & element2.keys()

    n = len(common_keys)

    products = []
    element1_notes = []
    element2_notes = []

    for key in common_keys :
        products.append(element1[key] * element2[key])
        element1_notes.append(element1[key])
        element2_notes.append(element2[key])

    element1_notes_squared = list(map((lambda x: x **2), element1_notes))
    element2_notes_squared = list(map((lambda x: x **2), element2_notes))

    diviseur = sqrt((n*sum(element1_notes_squared)- sum(element1_notes)**2)*(n*sum(element2_notes_squared)- sum(element2_notes)**2))
    
    if diviseur == 0: return 0

    r = (n*sum(products) - (sum(element1_notes)*sum(element2_notes)))/diviseur

    return r

# fonction retournant la liste des mots d'un article après l'avoir assaini en le débarrassant des caractères spéciaux et des majuscules
def sanitize_text(text : str):
    return re.sub(r"[^a-zA-Z0-9éèêëÉÈÊËàâäÂÀÄîïÎÏûùüÛÙÜôöÔÖÿŸçÇœŒ]", " ", text.lower()).split()

# fonction retournant le nombre d'occurences d'un mot dans une liste de mots
def text_words_occurrence(words : list[str]):
    
    words_occurrence = {}
    
    for word in words:
        words_occurrence[word] = words.count(word)
        words = list(filter(lambda a: a != word, words))

    return words_occurrence


def process():
    
    articles_names = os.listdir('wiki/')
    
    articles = {}
    word_appearance = {}

    all_words = []    

    for article in articles_names:
        file = open("wiki/" + article, "r")

        sanitized_text = sanitize_text(file.read())

        all_words += sanitized_text

        articles[article] = text_words_occurrence(sanitized_text)
    
    all_words = set(all_words)

    # déterminer le pourcentage d'apparution d'un mot dans les différents articles
    for word in all_words:
        
        word_appearance[word] = 0
        for article in articles:
            if word in articles[article] : word_appearance[word] += 1
        word_appearance[word] = (word_appearance[word] / len(articles_names)) * 100
    
    # filtrer les articles n'ayant pas un pourcentage d'apparution compris entre 10 et 50%
    words_to_ignore = {key: value for key, value in word_appearance.items() if value < 10 or value > 50}

    articles_similarity = {}

    # filtrer les articles en retirant les occurences des mots à ignorer
    for article in articles:
      articles[article] = {key: value for key, value in articles[article].items() if key not in words_to_ignore.keys()}

    # déterminier la similarité des articles entre eux
    for article in articles:
      articles_similarity[article] = {}

      for comparision_article in articles:
          if comparision_article == article: continue
          articles_similarity[article][comparision_article] = pearson(articles[article], articles[comparision_article])

    print(articles_similarity)


process()  