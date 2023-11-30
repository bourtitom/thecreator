class PNJ:
    def __init__(self, prenom, nom, age, marchand, histoire):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.marchand = marchand
        self.histoire = histoire

    def parler(self, message):
        return f"{self.nom} {self.prenom}: {message}"

liste_pnj = [
    PNJ("Thorne", "Sablelock", age=30, marchand=False, histoire="Histoire de Thorne"),
    PNJ("Seren", "Frostshade", age=22, marchand=True, histoire="Histoire de Seren"),
    # Ajoutez d'autres PNJ avec leurs propres informations
]

# Exposer la liste des PNJ en dehors du module
liste_pnj_global = liste_pnj

# Créer des variables pour chaque PNJ
Thorne = liste_pnj_global[0]
Seren = liste_pnj_global[1]

# Maintenant, vous pouvez utiliser Thorne et Seren comme des objets PNJ distincts
histoire_thorne = Thorne.histoire
histoire_seren = Seren.histoire

print(histoire_thorne)
print(histoire_seren)
