import discord
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
# verifier si le bot s'est bien connecter 
@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecter")

    try:
        synced = await bot.tree.sync(guild = discord.Object(id=1177549504883466340))
        # affichage de tout les commandes fonctionnel
        print(f"Synced {(len(synced))} commands")

    except Exception as e:
        print(e)
# premiere commande de test
@bot.tree.command(guild = discord.Object(id= 1177549504883466340), name = "test" , description = "test")
async def test_slash(interaction : discord.interactions):
    await interaction.response.send_message('TEST !')



# token du bot (a changer de place avec dotenv)
bot.run("MTE3NzYxOTExODg1NDI0NjQ4Mg.GHWPb7.I7KeKJ2oZqmuzywo1rOB1TPwPXNqV58CYZu3q4")