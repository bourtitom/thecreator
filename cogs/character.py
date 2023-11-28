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

class Stats():
     def __init__(self):
          ...

    # LES CLASSES
class ChoiseClasses(discord.ui.Select):
	def __init__(self):
		options = [
            discord.SelectOption(label= "Classe guerrier"),
            discord.SelectOption(label= "Classe archer", value = "archer"),
            discord.SelectOption(label= "Classe voleur", value = "voleur"),
            discord.SelectOption(label= "Classe magicien", value = "magicien"),
             ]
		super().__init__(placeholder = "Choisis ta classes", options = options, min_values = 1, max_values = 1)
	async def callback(self,interaction : discord.interactions):
         await interaction.response.send_message(f"Vous avez choisis la classe {self.values[0]}")
         

class ClassesView(discord.ui.View):
    def __init__ (self):
        super().__init__()
        self.add_item(ChoiseClasses())
