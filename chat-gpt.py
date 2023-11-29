import discord
import openai
import os
from discord.ext import commands

class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ask")
    async def ask_for_response(self, ctx, *, question: str):
        await ctx.defer()

        message = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "systeme", "content": "Tu es un bot discord"},
                {"role": "user", "content": question}
            ]
        )

        response = message["choices"][0]["message"]["content"]

        return await ctx.send(response)
