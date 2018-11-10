# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time
import shlex


# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Loci", command_prefix="-")
client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__,
                                                                               platform.python_version()))
    print('--------')
    print('Invite Link for {}:'.format(client.user.name))
    print('www.invite.loci.usa.cc'.format(client.user.id))
    print('--------')
    print('Support Discord Server: www.join.loci.usa.cc')
    print('--------')
    print('Running Loci v0.1')  # Version Number!
    print('Created by Arua Staff')
    return await client.change_presence(game=discord.Game(name='with string'))


@client.command()
async def ping(*args):
    await client.say(":ping_pong: Pong!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'give me admin':
        role = get(message.server.roles, name='Member')
        await client.add_roles(message.author, role)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.orange()
    )
    embed.set_author(name=':robot_face: General')
    embed.add_field(name='ping', value='Returns Pong!', inline=False)

    await client.send_message(author, embed=embed)





client.run('NTAzNjUxNzgzMzE1NDIzMjMy.DsdTmg.V_A5BRloa5k_hE5MUTdZgFID5ZI')

