import discord
from cogs import character
from discord.ext.commands import Context
from discord.ui import Button, View
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
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
# verifier si le bot s'est bien connecter 
@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecter")

    try:
        synced = await bot.tree.sync(guild = discord.Object(id=servId))
        # affichage de tout les commandes fonctionnel
        print(f"Synced {(len(synced))} commands")

    except Exception as e:
        print(e)
# detection du owner du serveur   
def is_owner(interaction):
        return interaction.user.id == interaction.guild.owner.id

# premiere commande de test
@bot.tree.command(guild = discord.Object(id= servId), name = "test" , description = "test",)
async def test_slash(interaction : discord.interactions):
    await interaction.response.send_message('TEST !')


@bot.tree.command(guild = discord.Object(id= servId), name = "latence" , description = "Avoir la latence du bot",)
@commands.has_permissions(administrator=True)
async def latence(interaction : discord.interactions):
    latency = bot.latency
    embed = discord.Embed(title = "**Latence**")
    embed.set_thumbnail(url ="https://images.frandroid.com/wp-content/uploads/2021/03/latence-reseau-lag.png")
    embed.add_field(name="Latence du bot : ",value=f"**{latency}**")
    await interaction.response.send_message(embed = embed)




@bot.tree.command(guild = discord.Object(id= servId), name = "start" , description = "Commencer l'aventure",)
@app_commands.describe(prenom = "prenom du perso", nom = "nom du perso", sexes = "t'as quoi entre les jambes", races = "ton ethnie", classes = "quelle classes tu vas incarné")
@app_commands.choices(sexes=[
    discord.app_commands.Choice(name='Homme', value='homme'),
    discord.app_commands.Choice(name='Femme', value='femme'),
    discord.app_commands.Choice(name='Autre', value='autre')
], races = [
     discord.app_commands.Choice(name='Guerrier' , value='guerrier'),
     discord.app_commands.Choice(name='Voleur' , value='voleur'),
     discord.app_commands.Choice(name='Archer' , value='archer'),
     discord.app_commands.Choice(name='Magicien' , value='magicien')
], classes = [
     discord.app_commands.Choice(name='Humains' , value='humains'),
     discord.app_commands.Choice(name='Elfes' , value='elfes'),
     discord.app_commands.Choice(name='Nains' , value='nains'),
     discord.app_commands.Choice(name='Demi-Géant' , value='demigeant'),
     discord.app_commands.Choice(name='Demi-Ange' , value='demiange'),
     discord.app_commands.Choice(name='Demi-Demon' , value='demidemon')

]
)
async def say(interaction: discord.Interaction, prenom: str, nom: str, sexes: app_commands.Choice[str], races: app_commands.Choice[str], classes: app_commands.Choice[str]):
    myperso = character.CreatePerso(prenom, nom, sexes, races, classes)
    
    await interaction.response.send_message(f"Très Bien: `{myperso.prenom} {myperso.nom}`")


# token du bot (a changer de place avec dotenv)
bot.run(TOKEN)