import discord
from cogs import character
from discord.ext.commands import Context
from discord import app_commands
from discord.ext import commands
from decouple import config
import os

discord_token = config('DISCORD_TOKEN')

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

# token du bot (a changer de place avec dotenv)
bot.run(discord_token)