class PNJ:
    def __init__(self, nom, prenom, age, marchant ):
        self.nom = nom
        self.age = age
        self.marchant = marchant
        self.prenom = prenom

    def parler(self, message):
        return f"{self.nom} {self.prenom}: {message}"

liste_pnj = [
    PNJ("Thorne","Sablelock", age = 30, marchant = False, ),
    PNJ("Seren","Frostshade", age = 22, marchant= True, ),
]