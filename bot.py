import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Alt Gen | .help | v0,1'))

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content == ".minecraft":
        await client.send_message(message.author, "**Alt Generator** \n Here is your Minecraft Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ")
    if message.content == ".special":
        await client.send_message(message.author, "**Alt Generator** \n Here is your Special Alt! \n email:pass \n \n Made by BlockBuster594✓ᵛᵉʳᶦᶠᶦᵉᵈ#6784 ")
    if message.content == ".help":
        await client.send_message(message.channel, "**Commands** \n \n**.help** \n Show this. \n \n**.minecraft** \n Gives you a free Minecraft alt. \n \n**.special** \n Gives you a free Proxy list. \n \n**.shop** \n Sends the shop link. \n \n**.invite** \n Invite the Alt Generator to your own server.")
    if message.content == ".shop":
        await client.send_message(message.channel, "**Shop**: \nhttps://selly.gg/@Refresh")
    if message.content == ".invite":
        await client.send_message(message.channel, "this is the bots invite link: ```https://discordapp.com/oauth2/authorize?&client_id=509798730942382080&scope=bot&permissions=8``` ")

client.run("NTA5Nzk4NzMwOTQyMzgyMDgw.DshoYw.t2h6O_b66wCHm7Ij7P-unWy6nOg")
