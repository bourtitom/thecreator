import discord
from discord.ext import commands
from decouple import config
import os

# Récupérer le token depuis les variables d'environnement ou un fichier .env
discord_token = os.environ.get('DISCORD_TOKEN', config('DISCORD_TOKEN'))

# Initialiser le bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name} ({bot.user.id})')

# Commande simple pour répondre à "ping" avec "pong"
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Exécuter le bot avec le token
bot.run(discord_token)
