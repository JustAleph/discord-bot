import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "+")

@client.event
async def on_ready():
    await client.change_presence(game=discord.game(name='Alt Generator | v0,1'))
    print("De bot is klaar voor gebruik!")

@client.event
async def on_message(message):
    if message.content == "+minecraft":
        await client.send_message(message.author, random.choice([" Alt Generator \n Here is your Minecraft Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " Alt Generator \n Here is your Minecraft Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 "]))
    if message.content == "+special":
        await client.send_message(message.author, random.choice([" Alt Generator \n Here is your Special Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ", " Alt Generator \n Here is your Special Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 "]))
    if message.content == "+help":
        await client.send_message(message.channel, "Commands \n \n+help \n Show this. \n \n+minecraft \n Only works in the generator channel. \n \n+special \n Only works in the generator channel. \n \n+shop \n Sends the shop link.")
    if message.content == "+shop":
        await client.send_message(message.channel, "Shop: \nhttps://selly.gg/@Refresh")

client.run("NTA5Nzk4NzMwOTQyMzgyMDgw.DsivnQ.hbTCGaFoAoooAJaoL2Ul3_8c4SE")
