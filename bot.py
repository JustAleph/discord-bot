import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Alt Gen | .help | v0,01'))

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content == ".minecraft":
        await client.send_message(message.author, " Alt Generator \n Here is your Minecraft Alt! \n account \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ")
    if message.content == ".special":
        await client.send_message(message.author, " Alt Generator \n Here is your Special Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ")
    if message.content == ".help":
        await client.send_message(message.channel, "Commands \n \n.help \n Show this. \n \n.minecraft \n Only works in the generator channel. \n \n.special \n Only works in the generator channel. \n \n.shop \n Sends the shop link.")
    if message.content == ".shop":
        await client.send_message(message.channel, "Shop: \nhttps://selly.gg/@Refresh")
    if message.content == ".help":
        await client.send_message(message.channel, embed=embed)

@client.event
async def on_message(message):
    if message.content.startswith('.shop'):
        embed=discord.Embed(title="Click me to go to our alt shop!", url="https://selly.gg/@refresh", color=0x3498db)
        embed.set_author(name="Refresh Alts", icon_url="https://ibb.co/Nnbr5C4")
        embed.set_footer(text="Refresh Alts © 2018 all rights reserved")
        await client.send_message(message.channel, embed=embed)

client.run("NTA5Nzk4NzMwOTQyMzgyMDgw.DtwG7A.uX907ZYeCwDuaFZEASVi-RabJTw")
