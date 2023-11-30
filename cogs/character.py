import discord
from discord.ext.commands import Context
from discord import app_commands
from discord.ext import commands

# importation des intents du bot discord
intents = discord.Intents().all()
# initialisation du prefix du bot
bot = commands.Bot(command_prefix = '+', intents = intents)
# configuration des intents
intents.message_content = True
intents.guilds = True
intents.members = True
# lier l'appelle du bot a une variable
client = discord.Client(intents = intents)
# commande slash
tree = app_commands.CommandTree(client)

servId = 1177549504883466340
class Titles():
     def __init__(self, name , condition ,rank, bonus):
          self.name = name
          self.condition = condition
          self.rank = rank
          self.bonus = bonus

class Stats():
     def __init__(self, force ,agilite , endurance, mana, intelligence, sagesse,chance, charisme, reputation):
          self.force = force
          self.agilite = agilite
          self.endurance = endurance
          self.mana = mana
          self.intelligence = intelligence
          self.sagesse = sagesse
          self.chance = chance
          self.charisme = charisme
          self.reputation = reputation

    # LES CLASSES
class Classes():
	def __init__(self, name, weapons, statsbase):
         self.name = name
         if(name == "guerrier"):
            self.statsbase = Stats(3, 1, 3, 2, 1, 1, 2, 3, 1) # 17 pts
            self.weapons = 'Epee'
         elif(name == "voleur"):
            self.statsbase = Stats(2, 3, 1, 2, 2, 1, 3, 2, 1) # 17 pts
            self.weapons = 'Griffe'
         elif(name == "archer"):
            self.statsbase = Stats(1, 3, 1, 3, 2, 3, 2, 1, 1) # 17 pts
            self.weapons = 'Arc'
         elif(name == "magicien"):
            self.statsbase = Stats(1, 2, 2, 3, 3, 2, 2, 1, 1) # 17 pts
            self.weapons = 'Baton'


class CreatePerso(): ## /start Tom Bourti 
    def __init__(self, prenom, nom , sexes,races, classes):
         self.prenom = prenom
         self.nom = nom
         self.age = 10
         self.sexes = sexes
         self.races = races
         self.potentielle = 1
         self.classes = classes

class ChoiceBTN(discord.ui.Button):
    def __init__(self):
        options = [
            discord.Button(label= "Classe guerrier"),
            discord.Button(label= "Classe archer", value = "archer"),
            discord.Button(label= "Classe voleur", value = "voleur"),
            discord.Button(label= "Classe magicien", value = "magicien"),
             ]
        super().__init__(placeholder = "Choisis ta classes", options = options, min_values = 1, max_values = 1)
    async def callback(self,interaction : discord.interactions):
         await interaction.response.send_message(f"Vous avez choisis la classe {self.values[0]}")



