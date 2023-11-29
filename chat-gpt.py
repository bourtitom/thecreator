import discord
import openai
import dotenv,os
from discord.ext import commands

class ChatGPT(commands):
	def __init__(self, bot : commands.Bot):
		self.bot = bot

		openai.api_key = os.getenv('OPEN_AI_TOKEN')

	@commands.hybrid_command(name = "ask")
	async def ask_for_response(self,ctx : commands.Context, *, question : str):
		await ctx.defer()

		message = openai.ChatCompletion.create(
			model = "gpt-3.5-turbo",
			messages = [
				{"role": "systeme", "content": "Tu es un bot discord"},
				{"role": "user", "content": question}
			]
		)

		response = message["choices"][0]["message"]["content"]

		return await ctx.send(response)
	
async def setup(bot : commands.Bot):
	await bot.add_cog(ChatGPT(bot))