import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
from discord import Member    
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from discord.ext.commands import MissingPermissions

client = commands.Bot(command_prefix = "+")
client.remove_command("help")

@client.event
async def on_ready():
    activity = discord.Game(name="OctUp Gaming", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(client.user.name)
    print("Online")
    print("-------")

@client.command(pass_context=True)
@has_permission(manage_roles=True, kick_members=True)
async def text(ctx,*,message):
    await ctx.send(message)


@client.command(pass_context=True)
@has_permissions(manage_roles=True, kick_members=True)
async def embed(ctx,*,message,):
    embed = discord.Embed(description=message,colour=0xFF0909)
    await ctx.send(embed=embed)



client.run("ODE0ODU5OTQ4Njg5MTk1MDE4.YDj_dw.6q9r7LXop5NEJaY2e8-7F6qfMaA")
