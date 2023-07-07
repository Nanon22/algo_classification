## instructions

Cet exercice n'a pas été entièrement traité.
Il va jusqu'à la détermination des similarités entre les articles mais ne gère pas le "regroupement". Car n'ayant pas suffisamment bien compris ce principe.

à la racine du dossier `/Clustering` en executant la commande : `python clustering.py`. On obtient un dictionnaire sous la forme :

```{
  "article1" : {
    "article2" : dégré de similarité calculé avec Pearson
    "article3" : dégré de similarité calculé avec Pearson
    "article4" : dégré de similarité calculé avec Pearson
    "article5" : dégré de similarité calculé avec Pearson
  },
  "article2" : {
    "article1" : dégré de similarité calculé avec Pearson
    "article3" : dégré de similarité calculé avec Pearson
    "article4" : dégré de similarité calculé avec Pearson
    "article5" : dégré de similarité calculé avec Pearson
  },
  "article3" : {
    "article1" : dégré de similarité calculé avec Pearson
    "article2" : dégré de similarité calculé avec Pearson
    "article4" : dégré de similarité calculé avec Pearson
    "article5" : dégré de similarité calculé avec Pearson
  },
  "article4" : {
    "article1" : dégré de similarité calculé avec Pearson
    "article2" : dégré de similarité calculé avec Pearson
    "article3" : dégré de similarité calculé avec Pearson
    "article5" : dégré de similarité calculé avec Pearson
  },
  "article5" : {
    "article1" : dégré de similarité calculé avec Pearson
    "article2" : dégré de similarité calculé avec Pearson
    "article3" : dégré de similarité calculé avec Pearson
    "article4" : dégré de similarité calculé avec Pearson
  },
}
```

d'autres fonctions ayant servit à atteindre ce résultat ont été commmenté dans le fichier `clustering.py` pour faciliter leur compréhesion
