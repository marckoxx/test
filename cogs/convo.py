import discord
from discord.ext import commands

class Conversation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['Hello', 'HELLO', 'HI', 'Hi', 'hi'])
    async def hello(self, ctx):
        await ctx.send("Hello!")

    @commands.command()
    async def kekw(self, ctx):
        await ctx.send(':kekw:')

    @commands.command()
    async def sample(self, ctx):
        embed=discord.Embed(title="Sample Embed", description="This is sample embed", color=discord.Color.purple())
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Conversation(client))
