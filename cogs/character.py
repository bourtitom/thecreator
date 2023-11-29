import discord
from discord.ext import commands, app_commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='+', intents=intents)
tree = app_commands.CommandTree(bot)

servId = 1177549504883466340

# LES CLASSES
class ChoiseClasses(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Classe guerrier"),
            discord.SelectOption(label="Classe archer", value="archer"),
            discord.SelectOption(label="Classe voleur", value="voleur"),
            discord.SelectOption(label="Classe magicien", value="magicien"),
        ]
        super().__init__(placeholder="Choisis ta classe", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Vous avez choisi la classe {self.values[0]}")

class ClassesView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ChoiseClasses())

# Commande slash
@bot.tree.command(guild=discord.Object(id=servId), name="start", description="Commencer l'aventure")
async def classes(interaction: discord.Interaction):
    await interaction.response.send_message(view=ClassesView(), ephemeral=True)
