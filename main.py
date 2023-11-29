import discord
from cogs import character
from PNJ import pnj
import chatGPT
from discord.ext import commands
from decouple import config
import os

servId = 1177549504883466340

# Récupérer le token depuis les variables d'environnement ou un fichier .env
discord_token = os.environ.get('DISCORD_TOKEN', config('DISCORD_TOKEN'))

# Initialiser le bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    bot.load_extension("chatGPT")
    print(f'Connecté en tant que {bot.user.name} ({bot.user.id})')

# Commande simple pour répondre à "ping" avec "pong"
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

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

    # CREATION DU PERSONNAGE
@bot.tree.command(guild = discord.Object(id = servId), name = "start", description = "Commencer l'aventure")
async def classes(interaction: discord.Interaction):
    await interaction.response.send_message(view=character.ClassesView(),ephemeral = True)

@bot.command(name = "talk")
async def talk(ctx, nom_pnj, message):
    pnj_trouve = None
    for pnj in pnj.liste_pnj:
        if pnj.nom == nom_pnj:
            pnj_trouve = pnj
            break

    if pnj_trouve:
        # Utilisez l'API GPT-3.5 pour générer une réponse
        reponse_gpt = chatGPT.ask_for_response(message)
        await ctx.send(f"{pnj_trouve.nom}: {reponse_gpt}")
    else:
        await ctx.send("PNJ non trouvé.")

# Exécuter le bot avec le token
bot.run(discord_token)
