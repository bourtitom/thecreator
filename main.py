import discord
import os
import openai
from cogs import character
from PNJ import pnj
from discord.ext import commands
from discord import app_commands
from decouple import config
from dotenv import load_dotenv


servId = 1177549504883466340

# Récupérer le token depuis les variables d'environnement ou un fichier .env
discord_token = os.environ.get('DISCORD_TOKEN', config('DISCORD_TOKEN'))

# Initialiser le bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name} ({bot.user.id})')

    # Ajoutez la cog ChatGPT
    bot.add_cog(ChatGPT(bot))
    
    # Chargez l'extension ChatGPT
    bot.load_extension("chatGPT")

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

class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        openai.api_key = "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"

    async def ask_for_response(self, ctx, question: str):
        await ctx.defer()

        message = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=100,
            messages=[
                {"role": "system", "content": "tu es un humain l'lambda mais passionné de code"},
                {"role": "user", "content": question}
            ]
        )

        response = message["choices"][0]["message"]["content"]

        return response

@bot.command()
async def talk(ctx, prenom_pnj, *, message=None):
    if message is None:
        await ctx.send("Veuillez fournir un message.")
        return

    pnj_trouve = next((pnjSearch for pnjSearch in pnj.liste_pnj_global if pnjSearch.prenom == prenom_pnj), None)

    if pnj_trouve:
        # Créez une instance de la classe ChatGPT
        chat_gpt_instance = ChatGPT(bot)
        
        # Utilisez l'API GPT-3.5 pour générer une réponse
        reponse_gpt = await chat_gpt_instance.ask_for_response(ctx, question=message)
        
        # Affichez des informations sur le PNJ trouvé
        await ctx.send(f"{pnj_trouve.prenom} {pnj_trouve.nom}, Âge: {pnj_trouve.age}, Marchand: {pnj_trouve.marchand} : {reponse_gpt}")
    else:
        # Envoyez un message si le PNJ n'est pas trouvé
        print("ez")

def setup(bot):
    bot.add_cog(ChatGPT(bot))


@bot.tree.command(guild=discord.Object(id=servId), name="start", description="Commencer l'aventure")
@app_commands.describe(prenom="prenom du perso", nom="nom du perso", sexes="t'as quoi entre les jambes", races="ton ethnie", classes="quelle classes tu vas incarné")
@app_commands.choices(sexes=[
    discord.app_commands.Choice(name='Homme', value='homme'),
    discord.app_commands.Choice(name='Femme', value='femme'),
    discord.app_commands.Choice(name='Autre', value='autre')
], races=[
    discord.app_commands.Choice(name='Humains', value='humains'),
    discord.app_commands.Choice(name='Elfes', value='elfes'),
    discord.app_commands.Choice(name='Nains', value='nains'),
    discord.app_commands.Choice(name='Demi-Géant', value='demigeant'),
    discord.app_commands.Choice(name='Demi-Ange', value='demiange'),
    discord.app_commands.Choice(name='Demi-Demon', value='demidemon')
], classes=[
    discord.app_commands.Choice(name='Guerrier', value='guerrier'),
    discord.app_commands.Choice(name='Voleur', value='voleur'),
    discord.app_commands.Choice(name='Archer', value='archer'),
    discord.app_commands.Choice(name='Magicien', value='magicien')
])
async def say(interaction: discord.Interaction, prenom: str, nom: str, sexes: app_commands.Choice[str], races: app_commands.Choice[str], classes: app_commands.Choice[str]):
    myperso = character.CreatePerso(prenom, nom, sexes, races, classes)
    embed = discord.Embed(title="Bienvenue dans le monde de Haxril", description="N'hesite pas a faire /lore pour avoir connaitre l'histoire du monde", colour=discord.Colour.random())
    url = None
    if myperso.classes == "guerrier": 
        url ="https://cdn.discordapp.com/attachments/1178679100358013020/1178679100622262272/dragonica-warrior.png?ex=65770574&is=65649074&hm=c619c31d4d4c0e872e405a77558b7c88c640350db413e3420e31871e816a62cb&"
    elif myperso.classes == "voleur":
        url ="https://media.discordapp.net/attachments/1178679175402500096/1178679175540920540/image.png?ex=65770586&is=65649086&hm=ff4947497207a4aaf7c380ca81f5af8ef15497324a14651f8428c3c79f9229e5&=&format=webp&quality=lossless&width=520&height=600"
    elif myperso.classes == "archer":
        url ="https://media.discordapp.net/attachments/1178678739366858812/1178678739601735801/image.png?ex=6577051e&is=6564901e&hm=3b6b5cf043c8d13d01bcd95c23f8109330c26e67c09a6e83b50d6835b6b6f1ec&=&format=webp&quality=lossless&width=520&height=600"
    elif myperso.classes == "magicien":
        url ="https://media.discordapp.net/attachments/1178677733279146095/1178677733862146108/dragonica-magician.png?ex=6577042e&is=65648f2e&hm=67b87c6337af458c94f931cc355a77430d3d31db8eba4d39ce38e4919dd47aee&=&format=webp&quality=lossless&width=520&height=600"
    elif myperso.classes == "chaman":
        url ="https://cdn.discordapp.com/attachments/1178978706342023238/1178978706467864617/image.png?ex=65781c7b&is=6565a77b&hm=b3502700c842c147e73bcf02787227bf8e10aeb45c5c1637461957b280f10207&"

    embed.set_thumbnail(url=url)
    embed.add_field(name="Prenom Nom", value="Guerrier")

    embed.set_footer(text="Create by The Creator")

    await interaction.response.send_message(f"Très Bien: `{myperso.prenom} {myperso.nom}`" , embed=embed)


# Exécuter le bot avec le token
bot.run(discord_token)
