import math
class Noeud :
    def __init__(self,valeur):
        self.valeur=valeur
        self.enfants=[]
    def ajouter_enfants(self,enfants) :
        self.enfants.append(enfants)
    def afficher(self):
        print(self.valeur ,end="")
        for enfants in self.enfants :
            enfants.afficher()
    def evaluer(self,variables):
        if isinstance(self.valeurs,(int,float)) :
            return float(self.valeur)
        if self.valeur=="+":
            return self.enfants[0].evaluer(variables)+self.enfants[1].evaluer(variables)
        elif self.valeur=="-" :
            return self.variables[0].evaluer(va)
   



