import discord
from cogs import character
from discord.ext.commands import Context
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
 

@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))
    await ctx.message.delete()
    print(f"{ctx.message.author} cette utilisateur a utiliser la commande say pour ecrire {texte}")

# CREATION DU PERSONNAGE
@bot.tree.command(guild = discord.Object(id = servId), name = "start", description = "Commencer l'aventure")
async def classes(interaction: discord.Interaction):
    await interaction.response.send_message(view=character.ClassesView(),ephemeral = True)

# token du bot (a changer de place avec dotenv)
bot.run(TOKEN)