import aiohttp
import discord
from discord.ext import commands
import json


class Swanson(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ron Swanson cog online')

    # Commands
    @commands.command()
    async def swanson(self, ctx):
        async with aiohttp.ClientSession() as session:
            data = await session.get('https://ron-swanson-quotes.herokuapp.com/v2/quotes')
            data = await data.json()
            quote = data[0]
        embed = discord.Embed(description=quote)
        # await ctx.message.delete()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Swanson(client))