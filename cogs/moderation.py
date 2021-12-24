import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send("`" + str(amount) + " messages have been deleted`")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title = (f'Error!'), description = ('Please provide the number of messages you wish to delete.'), color = discord.Color.purple())
            await ctx.send(embed = embed)

    @commands.command()
    async def kick(self, ctx, member : commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')

    @commands.command()
    async def ban(self, ctx, member : commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'User {user.mention} has been unbanned.')
                return
    
def setup(client):
    client.add_cog(Misc(client))
