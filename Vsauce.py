import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(client, message):
    with open('/home/mitsuru/Documents/Projects/vsauce/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix= get_prefix, intents = intents)
status = cycle(['Devil May Cry 3 Special Edition', "Devil May Cry 4 Special Edition", 'Devil May Cry 5 Special Edition'])

@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.online, activity=discord.Game('Devil May Cry 5 Special Edition'))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "<"

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Changed prefix to {prefix}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title = ('Error!'), description = ("Oh no! That command doesn't exist yet!"), color = discord.Color.purple())
        await ctx.send(embed = embed)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = (f'{extension} has been loaded.'), color = discord.Color.purple())
    await ctx.send(embed = embed)

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title = (f'{extension} has been unloaded.'), color = discord.Color.purple())
    await ctx.send(embed = embed)

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title = (f'{extension} has been reloaded.'), color = discord.Color.purple())
    await ctx.send(embed=embed)

def is_it_me(ctx):
    return ctx.author.id == 415482851388030978

@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hello master {ctx.message.author.mention}')

@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('/home/mitsuru/Documents/Projects/vsauce/cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('')
