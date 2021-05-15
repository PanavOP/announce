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
    activity = discord.Game(name="Stand Off 2", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(client.user.name)
    print("Online")
    print("-------")

@client.command(pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def text(ctx,*,message):
    await ctx.message.delete()
    await ctx.send(message)


@client.command(pass_context=True)
@has_permissions(manage_roles=True, ban_members=True)
async def embed(ctx,*,message,):
    embed = discord.Embed(description=message,colour=0xFF0909)
    await ctx.message.delete()
    await ctx.send(embed=embed)



client.run("ODQyNzg1MDI0NTk1NTkxMTg5.YJ6WuA.Fp1RNAo4whCbhW7jVODUXp8g05I")


