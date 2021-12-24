import discord
import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', 'tanong:', 'Tanong:'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is Certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.',
                    'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.',
                    'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
                    "Don't count on it.", 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.',
                    'Gago ka ba?', 'Haha no.', ':kekw::kekw::kekw::kekw:']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(Games(client))