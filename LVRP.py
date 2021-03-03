import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord.ext.commands import has_permissions

client = commands.Bot(command_prefix = "+")
client.remove_command("help")

@client.event
async def on_ready():
    print(client.user.name)
    print("Online")
    print("-------")

@client.command(pass_context=True)
async def lvrptext(ctx,message):
    await ctx.send(message)

@client.command(pass_context=True)
async def lvrpembed(ctx,*,message,):
    embed = discord.Embed(description=message,colour=0xFF0909)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def deletethis(ctx):
    await Bot.say('Command received')
    await Bot.delete_message(ctx.message)
    await Bot.say('Message deleted')


client.run("ODE1MTAyMjQ3MTMwMTAzODI4.YDnhHw.iFaucptuvPG1l5M7Idgqc_O4D14")
