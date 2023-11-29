import discord
from cogs import character
from discord.ext import commands, app_commands
from decouple import config
import os

# Récupérer le token depuis les variables d'environnement ou un fichier .env
discord_token = os.environ.get('DISCORD_TOKEN', config('DISCORD_TOKEN'))

# importation des intents du bot discord
intents = discord.Intents().all()

# initialisation du prefix du bot
bot = commands.Bot(command_prefix='+', intents=intents)

# lier l'appelle du bot a une variable
client = discord.Client(intents=intents)

# commande slash
tree = app_commands.CommandTree(client)

servId = 1177549504883466340

# Port d'écoute pour Heroku
port = int(os.environ.get('PORT', 5000))

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name} ({bot.user.id})')

# Décorateur pour vérifier si l'utilisateur est le propriétaire du serveur
def is_owner(interaction):
    return interaction.user.id == interaction.guild.owner.id

# Première commande de test
@bot.tree.command(guild=discord.Object(id=servId), name="test", description="test")
@commands.check(is_owner)
async def test_slash(interaction: discord.Interaction):
    await interaction.response.send_message('TEST !')

# Commande pour obtenir la latence du bot (avec autorisation d'administrateur)
@bot.tree.command(guild=discord.Object(id=servId), name="latence", description="Avoir la latence du bot")
@commands.has_permissions(administrator=True)
async def latence(interaction: discord.Interaction):
    latency = bot.latency
    embed = discord.Embed(title="**Latence**")
    embed.set_thumbnail(url="https://images.frandroid.com/wp-content/uploads/2021/03/latence-reseau-lag.png")
    embed.add_field(name="Latence du bot : ", value=f"**{latency}**")
    await interaction.response.send_message(embed=embed)

# CREATION DU PERSONNAGE
@bot.tree.command(guild=discord.Object(id=servId), name="start", description="Commencer l'aventure")
async def classes(interaction: discord.Interaction):
    await interaction.response.send_message(view=character.ClassesView(), ephemeral=True)

# Démarrage du bot
bot.run(discord_token, port=port)
