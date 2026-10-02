from noeud.py import Noeud
#création des feuilles de l'abre
deux=Noeud(2)
y=Noeud("y")
addition=Noeud("+")
addition.ajouter_enfants(deux)
addition.ajouter_enfants(y)
expression=Noeud("exp")
expression.ajouter_enfants(addition)
expression.afficher()