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

@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))
    await ctx.message.delete()
    print(f"{ctx.message.author} cette utilisateur a utiliser la commande say pour ecrire {texte}")



    # CREATION DU PERSONNAGE

@bot.tree.command(guild = discord.Object(id = servId), name = "start", description = "Commencer l'aventure")
async def classes(interaction: discord.Interaction):
    await interaction.response.send_message(view=ClassesView(),ephemeral = True)


    # LES CLASSES
class Classes(discord.ui.Select):
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
        self.add_item(Classes())





# token du bot (a changer de place avec dotenv)
bot.run("MTE3NzYxOTExODg1NDI0NjQ4Mg.GHWPb7.I7KeKJ2oZqmuzywo1rOB1TPwPXNqV58CYZu3q4")