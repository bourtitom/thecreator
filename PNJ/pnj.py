class PNJ:
    def __init__(self, prenom, nom, age, marchant ):
        self.nom = nom
        self.age = age
        self.marchant = marchant
        self.prenom = prenom

    def parler(self, message):
        return f"{self.nom} {self.prenom}: {message}"

liste_pnj = [
    PNJ(prenom = "Thorne",nom = "Sablelock", age = 30, marchant = False, ),
    PNJ(prenom = "Seren",nom = "Frostshade", age = 22, marchant = True, ),
]