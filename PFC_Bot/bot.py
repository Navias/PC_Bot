import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


# Needs to be changed to actual server when future
id = client.get_guild(656611518879760424/656611518879760427)


@client.event
async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), name='general')
    await channel.send("Bot is working!")

bot = commands.Bot(command_prefix='$')
# ctx = context and a command must have at least one parameter ctx


@bot.command(name='ping', help='Server Ping')
# errors ping correct first but get NaN error
async def ping(ctx):
    await ctx.send(f'Server Ping! {round(bot.latency * 1000)}ms')


@bot.command(name='about', help='About the Bot')
async def intro(ctx):
    introduction = [
     ('Hello PFC User!', 'This about is a admin and stock analysis tool'),
    ]
    response = random.choice(introduction)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling a dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
        ]
    await ctx.send(', '.join(dice))


@bot.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@bot.command(name='send_dm')
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)


# @bot.command(name='users', help='Getting Number of Members in a Server')
# async def on_message(ctx):
#     id = client.get_guild(id)
#     response = (id.member_count)
#     await ctx.send(response)

# @client.event
# async def on_member_join(member):
#     for channel in member.guild.channels:
#         if str(channel) == "General":
# await channel.send_message
# (f"""Welcome to general channel {member.mention}""")

bot.run(TOKEN)
